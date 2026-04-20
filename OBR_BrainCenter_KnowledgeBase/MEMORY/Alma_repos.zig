const std = @import("std");

pub const Station = struct {
    name: []const u8,
    local_path: []const u8,
    remote_url: []const u8,
};

pub const stations = [_]Station{
    .{ .name = "CORE", .local_path = "C:/Users/Cicero/LOGOS-X", .remote_url = "https://github.com/cicerolemos-tito/LOGOS-X.git" },
    .{ .name = "SQUAD_FACTORY", .local_path = "C:/Users/Cicero/LOGOS-X/APP_Production_ReadyTools/APP_SquadFactory_MultiAgentManager", .remote_url = "https://github.com/cicerolemos-tito/logos-x-squad-factory.git" },
    .{ .name = "CLAW_HARNESS", .local_path = "C:/Users/Cicero/LOGOS-X/APP_Production_ReadyTools/APP_ClawHarness_RustOrchestrator", .remote_url = "https://github.com/cicerolemos-tito/logos-x-claw.git" },
    .{ .name = "MEMORY_ENGINE", .local_path = "C:/Users/Cicero/LOGOS-X/APP_Production_ReadyTools/APP_MemoryEngine_VectorSearch", .remote_url = "https://github.com/cicerolemos-tito/logos-x-memory.git" },
    .{ .name = "LAB_EXPERIMENTAL", .local_path = "C:/Users/Cicero/LOGOS-X/PRJ_SquadSandbox_ExperimentalLab", .remote_url = "https://github.com/cicerolemos-tito/logos-x-sandbox.git" }
};

// LEI 24: Toda nova pasta que ultrapasse 50MB ou tenha ciclo proprio DEVE ser registrada como uma Station.
