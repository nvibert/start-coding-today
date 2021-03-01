# Written to monitor desktop logins during TechSummit 2021 Start Coding: Today session

# Required Horizon module
Import-Module VMware.VimAutomation.HorizonView

# User Configuration
$hzUser = ""
$hzPass = ""
$hzDomain = ""
$hzConn = ""
$poolName =  ""
$slackWebhook = 'https://hooks.slack.com/services/xxx'

# Connect to the Horizon View server
$hzServer = Connect-HVServer -server $hzConn -User $hzUser -Password $hzPass -Domain $hzDomain

# Execute loop how many times
$MAX_ITERATIONS = 120

# Pause for how long after each loop - i.e. every 5 seconds for 120 iterations means the script runs for 10 minutes
$SLEEP_INTERVAL_IN_SECONDS = 5

$numIterations = 1
while ( $numIterations -le $MAX_ITERATIONS )
{
    Write-Host "Iteration" $numIterations "of" $MAX_ITERATIONS
    $allVMs = Get-HVMachineSummary -PoolName $PoolName | select -ExpandProperty Base | Select-Object Name,UserName, BasicState
    $totalVMs = $allVMs.length
    $connectedVMs = 0
    foreach ($vm in $allVMs)
    {
        # Find and count VMs that show CONNECTED state
        if ( $vm.BasicState -eq "CONNECTED")
        {
            $connectedVMs += 1
            write-Host $vm.Name $vm.NamesData.UserName $vm.BasicState 
        }
    }
    $curTime = Get-Date
    $msg = $curTime.toString() + " - Pool '" + $poolName + "' connected desktops: " + $connectedVMs + " of " + $totalVMs
    Write-Host $msg
    $body = ConvertTo-Json @{
        text = $msg
    }

    # Post via Slack webhook
    try {
        Invoke-RestMethod -uri $slackWebhook -Method Post -body $body -ContentType 'application/json' 
    } catch {
        Write-Host "Unable to invoke webhook"
    }

    $numIterations += 1
    Write-Host "Sleeping..."
    Start-Sleep $SLEEP_INTERVAL_IN_SECONDS
}
Disconnect-HVServer -server $hzConn -confirm:$false