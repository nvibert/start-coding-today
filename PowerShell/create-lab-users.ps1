# Allows us to use the ActiveDirectory module, a set of cmdlets Microsoft provides for AD operations
Import-Module ActiveDirectory

# First student number
$StartNum = 1

# Last student number
$EndNum = 32

# Create the new accounts on this domain controller
$DCName = "dc01.set.local"

# Organization Unit for our accounts
$OUPath = "OU=TechSummit,OU=Users,OU=SET AMER,DC=set,DC=local"

# Add new users to this group for desktop entitlement 
$VDIGroup = "Horizon TechSummit AMER"

# Prompt the operator for a password to set on the accounts
$StudentPassword = Read-Host -AsSecureString "Enter student account password"

# Loop through the account numbers
for ($StudentNum = $StartNum; $StudentNum -le $EndNum; $StudentNum++)
{
    # Build the Active Directory name - i.e. Tech Summit01. 
    # PadLeft will turn the digit 1 into '01'.
    $Name = "Tech Summit" +  $StudentNum.ToString().PadLeft(2,'0')

    # Build the Active Directory account name i.e. techsummit01
    # PadLeft will turn the digit 1 into '01'.
    $SamAccountName = 'techsummit' +  $StudentNum.ToString().PadLeft(2,'0')

    # Display the names 
    write-host "Adding" $Name "("$SamAccountName ")"

    # Add the user to Active Directory.
    New-ADUser -Name $name -GivenName "Tech" -Surname "Summit" -AccountPassword $StudentPassword -SamAccountName $SamAccountName -Path $OUPath -Server $DCName -Enabled $TRUE

    # Add the user to the VDI group to entitle the user to a desktop
    Add-ADGroupMember -Identity $VDIGroup -Members $SamAccountName -Server $DCName
}

