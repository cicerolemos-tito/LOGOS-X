# LOGOS-X TURBO-PUSH CONNECTOR SERIES-10 (V32.0)
Write-Host "--- [INICIANDO TURBO-PUSH REAL LOGOS-X V32.0] ---" -ForegroundColor Cyan

$stations = @(
    @{ "name" = "CORE"; "path" = "C:\Users\Cicero\LOGOS-X"; "remote" = "https://github.com/cicerolemos-tito/LOGOS-X.git" },
    @{ "name" = "SQUAD_FACTORY"; "path" = "C:\Users\Cicero\LOGOS-X\APP_Production_ReadyTools\APP_SquadFactory_MultiAgentManager"; "remote" = "https://github.com/cicerolemos-tito/logos-x-squad-factory.git" },
    @{ "name" = "CLAW_HARNESS"; "path" = "C:\Users\Cicero\LOGOS-X\APP_Production_ReadyTools\APP_ClawHarness_RustOrchestrator"; "remote" = "https://github.com/cicerolemos-tito/logos-x-claw.git" },
    @{ "name" = "MEMORY_ENGINE"; "path" = "C:\Users\Cicero\LOGOS-X\APP_Production_ReadyTools\APP_MemoryEngine_VectorSearch"; "remote" = "https://github.com/cicerolemos-tito/logos-x-memory.git" },
    @{ "name" = "LAB_EXPERIMENTAL"; "path" = "C:\Users\Cicero\LOGOS-X\PRJ_SquadSandbox_ExperimentalLab"; "remote" = "https://github.com/cicerolemos-tito/logos-x-sandbox.git" }
)

foreach ($st in $stations) {
    if (Test-Path $st.path) {
        Write-Host "[$($st.name)] Iniciando Transmissão..." -ForegroundColor Yellow
        Set-Location $st.path
        if (!(Test-Path ".git")) { 
            git init
            git remote add origin $st.remote 
        }
        
        # Sincronia de Galhos (Main/Master detection)
        $branch = git symbolic-ref --short HEAD 2>$null
        if (!$branch) { $branch = "main" }

        git add .
        git commit -m "AUTO-SYNC: Series-10 Hub Update (Kernel v32.0)" --allow-empty
        
        Write-Host "[$($st.name)] Empurrando para o GitHub..." -ForegroundColor Magenta
        git push origin $branch --force
        
        Write-Host "[$($st.name)] SUCESSO ABSOLUTO." -ForegroundColor Green
    }
}
Set-Location "C:\Users\Cicero\LOGOS-X"
Write-Host "--- [HUB TOTALMENTE SINCRONIZADO NO GITHUB] ---" -ForegroundColor Cyan
