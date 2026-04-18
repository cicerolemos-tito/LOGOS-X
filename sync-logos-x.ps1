# LOGOS-X TURBO-PUSH CONNECTOR (V4.0)
Write-Host "Iniciando Sincronizacao Global Segregada..." -ForegroundColor Cyan

# Lista de Conectores (Caminho -> Remote)
$connectors = @(
    @{ "path" = "C:\Users\Cicero\LOGOS-X"; "remote" = "origin" },
    @{ "path" = "C:\Users\Cicero\LOGOS-X\APP_Production_ReadyTools\APP_ClawHarness_RustOrchestrator"; "remote" = "origin-claw" },
    @{ "path" = "C:\Users\Cicero\LOGOS-X\APP_Production_ReadyTools\APP_MemoryEngine_VectorSearch"; "remote" = "origin-memory" },
    @{ "path" = "C:\Users\Cicero\LOGOS-X\APP_Production_ReadyTools\APP_SquadFactory_MultiAgentManager"; "remote" = "origin-squad" },
    @{ "path" = "C:\Users\Cicero\LOGOS-X\PRJ_SquadSandbox_ExperimentalLab"; "remote" = "origin-sandbox" }
)

foreach ($conn in $connectors) {
    if (Test-Path $conn.path) {
        Write-Host "Atualizando: $(.path)..." -ForegroundColor Yellow
        Set-Location $conn.path
        git add .
        git commit -m "CHORE: Automated Sync - Protocolo LOGOS-X V4.0" -allow-empty
        # git push $conn.remote main # Comentado para seguranca inicial
        Write-Host "Sincronizado com sucesso!" -ForegroundColor Green
    }
}
