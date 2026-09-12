# 出典台帳

確認日: **2026-09-13**。公式ドキュメント／上流ソースに基づく比較。LLM接続・完走は未実測。

[読み方と対象範囲](../README.md) · [ローカル接続](local-models.md) · [コマンド](commands.md) · [放置運用](autonomy.md) · [個別詳細](details.md) · [出典](sources.md)

GitHubの出典は可能な限り確認時のコミットへ固定しています。Webドキュメントは随時更新されます。取得記録は [source-audit.json](../data/source-audit.json)、リポジトリの参照点は [upstream-revisions.json](../data/upstream-revisions.json) にあります。

| ID | 一次資料 | 確認日 |
| --- | --- | --- |
| codex-cli | [Codex CLI / slash commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | 2026-09-13 |
| codex-config | [Codex provider configuration](https://learn.chatgpt.com/docs/config-file/config-reference) | 2026-09-13 |
| claude-cli | [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) | 2026-09-13 |
| claude-interactive | [Claude Code interactive commands](https://code.claude.com/docs/en/interactive-mode) | 2026-09-13 |
| claude-loop | [Claude Code scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks) | 2026-09-13 |
| claude-local | [Ollama: Claude Code integration](https://docs.ollama.com/integrations/claude-code) | 2026-09-13 |
| grok-cli | [Grok Build CLI reference](https://docs.x.ai/build/cli/reference) | 2026-09-13 |
| grok-config | [Grok Build settings reference](https://docs.x.ai/build/settings/reference) | 2026-09-13 |
| grok-commands | [Grok Build modes and commands](https://docs.x.ai/build/modes-and-commands) | 2026-09-13 |
| grok-headless | [Grok Build headless / ACP](https://docs.x.ai/build/cli/headless-scripting) | 2026-09-13 |
| qwen-provider | [Qwen Code model providers](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/) | 2026-09-13 |
| qwen-commands | [Qwen Code commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) | 2026-09-13 |
| qwen-goal | [Qwen Code goals](https://qwenlm.github.io/qwen-code-docs/en/users/features/goals/) | 2026-09-13 |
| qwen-subagents | [Qwen Code subagents](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/) | 2026-09-13 |
| qwen-sandbox | [Qwen Code sandbox](https://qwenlm.github.io/qwen-code-docs/en/users/features/sandbox/) | 2026-09-13 |
| qwen-headless | [QwenLM/qwen-code: docs/users/features/headless.md](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | 2026-09-13 |
| opencode-cli | [OpenCode CLI (non-v2 docs)](https://opencode.ai/docs/cli/) | 2026-09-13 |
| opencode-tui | [OpenCode TUI](https://opencode.ai/docs/tui/) | 2026-09-13 |
| opencode-provider | [OpenCode providers](https://opencode.ai/docs/providers/) | 2026-09-13 |
| opencode-agents | [OpenCode agents](https://opencode.ai/docs/agents/) | 2026-09-13 |
| opencode-permission | [OpenCode permissions](https://opencode.ai/docs/permissions/) | 2026-09-13 |
| opencode-v2 | [OpenCode v2 providers (separate schema)](https://opencode.ai/v2/docs/providers) | 2026-09-13 |
| hermes-cli | [NousResearch/hermes-agent: website/docs/reference/cli-commands.md](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | 2026-09-13 |
| hermes-slash | [NousResearch/hermes-agent: website/docs/reference/slash-commands.md](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/slash-commands.md) | 2026-09-13 |
| hermes-local | [Hermes local Ollama endpoint](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup) | 2026-09-13 |
| hermes-goal | [Hermes persistent goals and quality gates](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) | 2026-09-13 |
| hermes-readme | [NousResearch/hermes-agent: README.md](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/README.md) | 2026-09-13 |
| dsh-cli | [deepseek-ai/deepseek-harness: apps/cli/reference/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | 2026-09-13 |
| dsh-providers | [deepseek-ai/deepseek-harness: docs/user/guide/providers.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/providers.md) | 2026-09-13 |
| dsh-goal | [deepseek-ai/deepseek-harness: packages/goal/command-goal/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/goal/command-goal/README.md) | 2026-09-13 |
| dsh-driver | [deepseek-ai/deepseek-harness: packages/goal/goal-round-driver/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/goal/goal-round-driver/README.md) | 2026-09-13 |
| dsh-plan | [deepseek-ai/deepseek-harness: packages/plan/plan-mode/README.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/plan/plan-mode/README.md) | 2026-09-13 |
| dsh-schedule | [deepseek-ai/deepseek-harness: docs/user/guide/schedule.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/schedule.md) | 2026-09-13 |
| dsh-python | [deepseek-ai/deepseek-harness: docs/user/guide/python-sdk.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/python-sdk.md) | 2026-09-13 |
| dsh-approval | [deepseek-ai/deepseek-harness: docs/subsystems/permission-presets.md](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/subsystems/permission-presets.md) | 2026-09-13 |
| dsh-announcement | [DeepSeek Harness developer preview](https://deepseek.com/harness/en/) | 2026-09-13 |
| pi-readme | [earendil-works/pi: packages/coding-agent/README.md](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | 2026-09-13 |
| pi-models | [earendil-works/pi: packages/coding-agent/docs/models.md](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/docs/models.md) | 2026-09-13 |
| pi-rpc | [Pi RPC mode](https://pi.dev/docs/latest/rpc) | 2026-09-13 |
| aider-models | [Aider supported LLMs](https://aider.chat/docs/llms.html) | 2026-09-13 |
| aider-openai | [Aider OpenAI-compatible APIs](https://aider.chat/docs/llms/openai-compat.html) | 2026-09-13 |
| aider-options | [Aider options](https://aider.chat/docs/config/options.html) | 2026-09-13 |
| aider-commands | [Aider chat commands](https://aider.chat/docs/usage/commands.html) | 2026-09-13 |
| aider-test | [Aider lint / test](https://aider.chat/docs/usage/lint-test.html) | 2026-09-13 |
| aider-modes | [Aider architect / editor](https://aider.chat/docs/usage/modes.html) | 2026-09-13 |
| oh-overview | [OpenHands components and legacy status](https://docs.openhands.dev/overview/introduction) | 2026-09-13 |
| oh-cli | [OpenHands legacy CLI reference](https://docs.openhands.dev/openhands/usage/cli/command-reference) | 2026-09-13 |
| oh-persist | [OpenHands SDK persistence](https://docs.openhands.dev/sdk/guides/convo-persistence) | 2026-09-13 |
| oh-api | [OpenHands SDK Conversation API](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.conversation) | 2026-09-13 |
| oh-security | [OpenHands SDK confirmation policy](https://docs.openhands.dev/sdk/guides/security) | 2026-09-13 |
| oh-delegate | [OpenHands file-based agents / delegation](https://docs.openhands.dev/sdk/guides/agent-file-based) | 2026-09-13 |
| oh-sdk | [OpenHands/software-agent-sdk: README.md](https://github.com/OpenHands/software-agent-sdk/blob/76e9e25078ed0ff7970f2c75e451274d3ed32bf2/README.md) | 2026-09-13 |
| goose-cli | [aaif-goose/goose: documentation/docs/guides/goose-cli-commands.md](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | 2026-09-13 |
| goose-provider | [aaif-goose/goose: documentation/docs/getting-started/providers.md](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/getting-started/providers.md) | 2026-09-13 |
| goose-config | [aaif-goose/goose: documentation/docs/guides/config-files.md](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/config-files.md) | 2026-09-13 |
| vibe-readme | [mistralai/mistral-vibe: README.md](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | 2026-09-13 |
| vibe-local | [Vibe offline models](https://docs.mistral.ai/vibe/code/cli/offline-models) | 2026-09-13 |
| vibe-commands | [Vibe commands / shortcuts](https://docs.mistral.ai/vibe/code/cli/commands-shortcuts) | 2026-09-13 |
| kilo-cli | [Kilo CLI reference](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | 2026-09-13 |
| kilo-commands | [Kilo CLI slash commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | 2026-09-13 |
| kilo-local | [Kilo local providers](https://kilo.ai/docs/automate/extending/local-models) | 2026-09-13 |
| kilo-models | [Kilo custom models](https://kilo.ai/docs/code-with-ai/agents/custom-models) | 2026-09-13 |
| cline-cli | [cline/cline: docs/cli/cli-reference.mdx](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) | 2026-09-13 |
| cline-readme | [cline/cline: apps/cli/README.md](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | 2026-09-13 |
| cline-local | [cline/cline: docs/running-models-locally/overview.mdx](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/running-models-locally/overview.mdx) | 2026-09-13 |
| gemini-cli | [Gemini CLI cheatsheet](https://geminicli.com/docs/cli/cli-reference/) | 2026-09-13 |
| gemini-auth | [Gemini CLI authentication](https://geminicli.com/docs/get-started/authentication/) | 2026-09-13 |
| gemini-plan | [Gemini CLI plan mode](https://geminicli.com/docs/cli/plan-mode/) | 2026-09-13 |
| gemini-config | [Gemini CLI configuration](https://geminicli.com/docs/reference/configuration/) | 2026-09-13 |
| claude-commands | [Claude Code current command catalog](https://code.claude.com/docs/en/commands) | 2026-09-13 |
| gemini-commands | [Gemini CLI command catalog](https://geminicli.com/docs/reference/commands/) | 2026-09-13 |
| oh-llm | [OpenHands SDK LLM API](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.llm) | 2026-09-13 |
| oh-condenser | [OpenHands Context Condenser](https://docs.openhands.dev/sdk/guides/context-condenser) | 2026-09-13 |
| oh-workspace | [OpenHands workspace API](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.workspace) | 2026-09-13 |
| goose-subagents | [Goose subagent tutorial](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/tutorials/subagents.md) | 2026-09-13 |
