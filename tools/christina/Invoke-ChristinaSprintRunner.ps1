param(
    [string]$ConfigPath = "config/christina.runner.json"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ConfigPath)) {
    throw "Christina configuration not found: $ConfigPath"
}

$config = Get-Content $ConfigPath -Raw | ConvertFrom-Json

Write-Host "=== Christina Sprint Runner ==="
Write-Host "Project : $($config.project)"
Write-Host "Mode    : $($config.mode)"
Write-Host "MaxItems: $($config.maxItems)"
Write-Host ""

$result = [ordered]@{
    mode = $config.mode
    maxItems = $config.maxItems
    reportPath = $config.reporting.outputDir
    autoMerge = $false
    selectedIssue = "SignalForge + ETS governance integration"
    nextAction = "Generate sprint report and governance review summary"
}

$result | ConvertTo-Json -Depth 5
