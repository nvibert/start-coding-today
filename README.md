# Start Coding Today 

## 2021 VMware TechSummit Session
Co-presented by Patrick Kremer and Nico Vibert.
This session will be presented at the internal VMware conference TechSummit.

## Objectives

In 25 minutes, attendees will be able to learn and practice coding.

## Requirements

A browser with Internet access.

That's it. No coding experience required. No need to get access to a vCenter as a simulated vCenter will be provided.

## What the attendee will do during the session:

* Learn the basic concepts behind REST APIs
* Run a PowerCLI script against a vCenter
* Run API calls with Postman against a vCenter
* Execute an API call with Python against a vCenter
* Deploy VMware resources with Terraform

## Session Structure

### Part 1 - Introduction

Welcome to the session. This session is for anyone who's never had the confidence or the motivation to learn to code. 
It's hard to get started with coding without a use case, a mentor, an environment you can learn and a safe place where there's no stupid questions.

This is a short session and this session is more of an introduction to coding for folks who have a background as infrastructure and virtualization administrators and would like to understand the 'art of the possible'. 

### Part 2 - APIs

// brief introduction to REST APIs
// CRUD

If you are on the live VMware training, access your virtual desktop
### Part 3a - Desktop Access

Access your VDI session at this [URL](https://desktop.vmc.ninja)

Usernames and passwords will be provided in the Zoom session.

### Part 3b - Preparation

### Part 4 - PowerCLI

PowerCLI is one of the most common tools to automate tasks against a VMware environment. PowerCLI abstracts the API calls by providing a command-line interface tool that is self-explanatory.

Open the PowerShell windows and run the following command:

    Connect-VIServer localhost -port 8989 -User Foo -Password Bar
    
You are now connected to a simulated vCenter (we used a tool called govc and vcsim to save the configuration of a real vCenter and restore it).

Now that you are connected, you can run multiple PowerCLI commands, such as:

    Get-VMHost

    Get-Folder

    Get-Datacenter

    Get-Datastore


You can run the following command to understand why cmdlets are supported:
`
Get-Command -Module *VMware*
`

As you are using a simulated vCenter, not all the commands will work. 
But some do and we can even create new items in the simulated vCenter. Let's try to create a new folder inside an existing folder. One way to do this is to create a PowerShell variable, using the '$' prefix.

    $VMFolder = Get-Folder -Type VM

Now you can refer to this variable in your next command:

    New-Folder "MyFolder" -Location $VMFolder

Great! You've just used some scripts to create vSphere resources over APIs. Yes, PowerCLI just executes some API calls under the hood but a lot of the complexity was hidden from you.

You can combine multiple PowerCLI commands into a single PowerShell script and the script will run everything for you. 

Navigate to the Folder /blablablabla and open the file to_be_confirmed.ps1

As you can see, the script will do the following:

    - create this
    - create that
    - create that
    - run some checks



### Part 5 - APIs

PowerCLI is very easy to use as you can see. But what PowerCLI only does is making API calls under the hood.

You will find easier to understand automation by building some understanding of API architectures.

Typically, API calls run a CRUD Action: Create, Read, Update or Delete.

For example:
- Create a VM
- Check the items of a content library
- Update the vSAN storage policy on a VM
- Remove a NSX network

Most API requests are made through a HTML request, which would be:

- PUT   ===== CREATE
- GET   ===== READ
- PATCH  ==== UPDATE
- DELETE ==== DELETE

When you browse any page on the web, you just make a HTTP GET request to get the contents of a webpage.

It's the same if you want to get the contents of a vCenter, it will just be a GET call.

When you submit a form online, you just make a HTTP POST request to submit your details.

It's same when you want to create a network with NSX over the APIs: you just make a HTTP POST Call, with the details about your network (subnet, mask, DHCP settings) in the body of the packet.
