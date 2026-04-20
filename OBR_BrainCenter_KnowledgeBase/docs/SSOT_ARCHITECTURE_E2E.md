# LOGOS-X SSOT ARCHITECTURE: END-TO-END PROCESS (V3.0)

1. **TRIGGER:** Agent Activation or Git Commit.
2. **PULSE CHECK:** System reads SSOT_PULSE.json.
3. **INJECTION:** ssot-projector.py sets environment variables.
4. **EMANATION:** All {{PULSE}} tags in Markdown/Code are dynamically resolved.
5. **HARDENING:** ssot-guardian.py purges any static version string found.

**SOVEREIGNTY:** Non-written, dynamic, and non-hardcoded context.
