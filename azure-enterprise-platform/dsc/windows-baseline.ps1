Configuration WindowsBaseline {
    Node localhost {
        WindowsFeature IIS {
            Name = "Web-Server"
            Ensure = "Present"
        }
    }
}

WindowsBaseline
Start-DscConfiguration -Path .\WindowsBaseline -Wait -Force

