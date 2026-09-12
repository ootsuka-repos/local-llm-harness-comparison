# 個別仕様・正式エイリアス

確認日: **2026-09-13**。公式ドキュメント／上流ソースに基づく比較。LLM接続・完走は未実測。

[読み方と対象範囲](../README.md) · [ローカル接続](local-models.md) · [コマンド](commands.md) · [放置運用](autonomy.md) · [個別詳細](details.md) · [出典](sources.md)

## Codex CLI

対象: CLI。手元の help は 0.154.0。クラウド／Desktop機能は別

公式: [https://developers.openai.com/codex/](https://developers.openai.com/codex/)

`codex --oss --local-provider ollama -m MODEL`。LM Studioも選択可。独自providerは`base_url`＋`wire_api = "responses"`。Chat Completionsだけのサーバーとは直接同一視しない。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) [codex-config](https://learn.chatgpt.com/docs/config-file/config-reference)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `codex` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| モデル選択 | MIXED | `--model MODEL` / `/model` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | `-m` = `--model` |
| 非対話実行 | CLI | `codex exec "PROMPT"` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | `codex e` = `codex exec` |
| 再開 | CLI | `codex resume --last` / `codex resume ID` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| 計画 | SLASH | `/plan [PROMPT]` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| 履歴圧縮 | SLASH | `/compact` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| 承認制御 | CLI | `--ask-for-approval never --sandbox workspace-write`。承認しない設定と隔離は別。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | `-a` = `--ask-for-approval`<br>`-s` = `--sandbox` |
| 目標まで継続 | SLASH | `/goal OBJECTIVE`、`/goal pause`、`/goal resume`。ローカルモデルでの継続品質は未実測。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| テスト・修正 | MODEL | テストを実行して失敗を修正するよう依頼。`codex review`はレビュー用でテスト合格ゲートではない。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| サブエージェント | MIXED | エージェント機能・設定で委譲。`codex agents`はセッション閲覧で、spawnコマンドではない。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) [codex-config](https://learn.chatgpt.com/docs/config-file/config-reference) | — |
| 定期・背景実行 | UNVERIFIED | この比較ではローカルCLIの定期実行コマンド未確定。外部schedulerで`codex exec`を起動可能。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| 実行上限 | CONFIG | providerの`request_max_retries` / `stream_max_retries`。壁時計制限は外部プロセス管理で補う。 [codex-config](https://learn.chatgpt.com/docs/config-file/config-reference) | — |
| 隔離 | CLI | `--sandbox workspace-write` / `read-only`。`--worktree`はGit分離でOS隔離ではない。 [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| 拡張・MCP | MIXED | `codex mcp`、`codex plugin`、`/skills` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |
| 機械可読出力 | CLI | `codex exec --json "PROMPT"` [codex-cli](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | — |

- 比較対象として掲載。ユーザーのローカル用候補からは希望どおり優先除外。
- `codex -p`はプロファイル指定。非対話プロンプト指定は`exec`。
- 全CLIフラグがすべてのサブコマンドへ伝播するとは限らない。

## Claude Code

対象: CLI。非Claudeモデル経路はOllama側の公式案内

公式: [https://code.claude.com/](https://code.claude.com/)

OllamaのAnthropic互換APIで接続。`ANTHROPIC_BASE_URL=http://localhost:11434`、`ANTHROPIC_AUTH_TOKEN=ollama`、`ANTHROPIC_API_KEY=""`を設定し`claude --model MODEL`。Chat Completionsのみなら変換層が必要。 [claude-local](https://docs.ollama.com/integrations/claude-code)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `claude` [claude-cli](https://code.claude.com/docs/en/cli-reference) | — |
| モデル選択 | MIXED | `--model MODEL` / `/model` [claude-cli](https://code.claude.com/docs/en/cli-reference) [claude-commands](https://code.claude.com/docs/en/commands) | — |
| 非対話実行 | CLI | `claude --print "PROMPT"` [claude-cli](https://code.claude.com/docs/en/cli-reference) | `-p` = `--print` |
| 再開 | CLI | `claude --continue` / `claude --resume ID` [claude-cli](https://code.claude.com/docs/en/cli-reference) | `-c` = `--continue`<br>`-r` = `--resume` |
| 計画 | MIXED | `--permission-mode plan` / `/plan` [claude-cli](https://code.claude.com/docs/en/cli-reference) [claude-commands](https://code.claude.com/docs/en/commands) | — |
| 履歴圧縮 | SLASH | `/compact [INSTRUCTIONS]` [claude-commands](https://code.claude.com/docs/en/commands) | — |
| 承認制御 | CLI | `--allowedTools`等で許可範囲を指定。全スキップは`--dangerously-skip-permissions`。 [claude-cli](https://code.claude.com/docs/en/cli-reference) | — |
| 目標まで継続 | SLASH | 通常のagent loop。`/loop`は反復／定期実行で、独立した成果検証の保証ではない。 [claude-loop](https://code.claude.com/docs/en/scheduled-tasks) | — |
| テスト・修正 | MIXED | シェルでテスト→修正を依頼。`/verify`は明示起動の検証skillで、決定的な必須ゲートとは別。 [claude-cli](https://code.claude.com/docs/en/cli-reference) [claude-commands](https://code.claude.com/docs/en/commands) | — |
| サブエージェント | MIXED | `--agents JSON` / agent定義ファイル、`/subtask TASK`でforked subagent。現行`/agents`は管理方法の案内。 [claude-cli](https://code.claude.com/docs/en/cli-reference) [claude-commands](https://code.claude.com/docs/en/commands) | — |
| 定期・背景実行 | SLASH | `/loop INTERVAL PROMPT`。セッション稼働中に発火。終了中は動かず、再開時の復元に例外あり。 [claude-loop](https://code.claude.com/docs/en/scheduled-tasks) | — |
| 実行上限 | CLI | printモードの`--max-turns N` / `--max-budget-usd N`。ローカルモデルの価格上限は時間制限の代用にしない。 [claude-cli](https://code.claude.com/docs/en/cli-reference) | — |
| 隔離 | SLASH | `/sandbox`。権限スキップとsandboxを混同しない。 [claude-commands](https://code.claude.com/docs/en/commands) | — |
| 拡張・MCP | MIXED | `claude mcp`、`/mcp`、`/skills`、hooks / plugins [claude-cli](https://code.claude.com/docs/en/cli-reference) [claude-commands](https://code.claude.com/docs/en/commands) | — |
| 機械可読出力 | CLI | `claude -p "PROMPT" --output-format json` / `stream-json` [claude-cli](https://code.claude.com/docs/en/cli-reference) | — |

- 非Claudeモデルで全機能が同等に動くというAnthropicの保証は確認していない。
- Ollama Cloudモデルを選ぶとローカル推論にはならない。
- ユーザーの希望により推奨候補とは別枠。

## Grok Build

対象: 公式`grok` CLI。非公式grok-code / grok-cliやGrok Code Fastモデルとは別

公式: [https://docs.x.ai/build/overview](https://docs.x.ai/build/overview)

`~/.grok/config.toml`の`[model.<id>]`に`base_url`、`model`、`api_backend`を設定。独自モデル経路あり。ローカルQwen実測は未実施。 [grok-config](https://docs.x.ai/build/settings/reference)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `grok` [grok-cli](https://docs.x.ai/build/cli/reference) | — |
| モデル選択 | MIXED | `--model MODEL` / `/model MODEL` [grok-cli](https://docs.x.ai/build/cli/reference) [grok-commands](https://docs.x.ai/build/modes-and-commands) | `-m` = `--model`<br>`/m` = `/model` |
| 非対話実行 | CLI | `grok --single "PROMPT"` [grok-headless](https://docs.x.ai/build/cli/headless-scripting) | `-p` = `--single` |
| 再開 | CLI | `grok --continue` / `grok --resume ID` [grok-cli](https://docs.x.ai/build/cli/reference) | `-c` = `--continue`<br>`-r` = `--resume` |
| 計画 | SLASH | `/plan [DESCRIPTION]` / `/view-plan` [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| 履歴圧縮 | SLASH | `/compact [CONTEXT]` [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| 承認制御 | CLI | `--always-approve`。denyルールやhooksは別に適用。 [grok-cli](https://docs.x.ai/build/cli/reference) [grok-commands](https://docs.x.ai/build/modes-and-commands) | `--yolo` = `--always-approve`<br>`--dangerously-skip-permissions` は互換別名 |
| 目標まで継続 | SLASH | `/workflow NAME`で保存workflowを実行・pause/resume。独立した完了検証の有無は未確認。 [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| テスト・修正 | MODEL | シェルでテスト→修正を依頼。workflowに手順を記述可能。 [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| サブエージェント | MIXED | `GROK_SUBAGENTS=1`、taskツール。`/tasks`で確認。 [grok-config](https://docs.x.ai/build/settings/reference) [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| 定期・背景実行 | SLASH | `/loop [INTERVAL] PROMPT`、`/tasks` [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| 実行上限 | MIXED | `--max-turns N`、modelごとの`max_retries` [grok-cli](https://docs.x.ai/build/cli/reference) [grok-config](https://docs.x.ai/build/settings/reference) | — |
| 隔離 | CLI | `--sandbox workspace` / `read-only` / `strict`。`--worktree`は別のGit分離。 [grok-cli](https://docs.x.ai/build/cli/reference) [grok-config](https://docs.x.ai/build/settings/reference) | — |
| 拡張・MCP | MIXED | `grok mcp`、`grok plugin`、`/skills`、hooks [grok-cli](https://docs.x.ai/build/cli/reference) [grok-commands](https://docs.x.ai/build/modes-and-commands) | — |
| 機械可読出力 | CLI | `--output-format json` / `streaming-json`、`grok agent stdio`はACP [grok-headless](https://docs.x.ai/build/cli/headless-scripting) | — |

- 「grokcode」は本比較では公式Grok Buildと解釈。
- `streaming-json`という綴り。他CLIの`stream-json`をそのまま使わない。
- 補助モデルやホスト側検索の設定もローカル化対象。カスタム推論先の指定だけで完全オフラインとは断定しない。

## Qwen Code

対象: 公式CLI。更新の速い現行docs / mainを参照

公式: [https://github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)

`qwen --auth-type openai --openai-base-url URL --openai-api-key KEY --model MODEL`。URLは通常`http://127.0.0.1:PORT/v1`。 [qwen-provider](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `qwen` [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | — |
| モデル選択 | MIXED | `--model MODEL` / `/model` [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) [qwen-commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) | `-m` = `--model` |
| 非対話実行 | CLI | `qwen --prompt "PROMPT"` [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | `-p` = `--prompt` |
| 再開 | CLI | `qwen --continue` / `qwen --resume ID`。headlessにも対応。 [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | — |
| 計画 | CLI | `--approval-mode plan` [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | — |
| 履歴圧縮 | SLASH | `/compress` [qwen-commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) | `/summarize` = `/compress` |
| 承認制御 | CLI | `--approval-mode yolo` / `--yolo`。`auto`は判定による承認で全許可とは異なる。 [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | `-y` = `--yolo` |
| 目標まで継続 | MIXED | `/goal OBJECTIVE`。headlessは`qwen -p "/goal OBJECTIVE"`。完了・blocked申告を検証役が判定。 [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) [qwen-goal](https://qwenlm.github.io/qwen-code-docs/en/users/features/goals/) | — |
| テスト・修正 | MODEL | テスト合格をGoalの検証条件に記載。テスト実行・修正はモデルのツール操作。 [qwen-goal](https://qwenlm.github.io/qwen-code-docs/en/users/features/goals/) | — |
| サブエージェント | MIXED | `/agents create` / `manage`、`/fork DIRECTIVE`、`/coordinate TASK`。subagentのモデル・権限設定に依存。 [qwen-commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) [qwen-subagents](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/) | — |
| 定期・背景実行 | SLASH | `/loop INTERVAL PROMPT`は同梱skill。`/tasks` / `/workflows`で背景作業を確認。 [qwen-commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) | — |
| 実行上限 | CLI | `--max-session-turns N` / `--max-wall-time 1h` / `--max-tool-calls N`。serve/ACPへ同じ上限が適用されると仮定しない。 [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | — |
| 隔離 | CLI | `--sandbox`。`--yolo`だけでは隔離されない。 [qwen-sandbox](https://qwenlm.github.io/qwen-code-docs/en/users/features/sandbox/) [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | — |
| 拡張・MCP | SLASH | `/mcp`、`/skills`。拡張の有効化状態に依存。 [qwen-commands](https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/) | — |
| 機械可読出力 | CLI | `--output-format json` / `stream-json` [qwen-headless](https://github.com/QwenLM/qwen-code/blob/3ba01990e13e9e8e14e147b60add50e0f972431a/docs/users/features/headless.md) | `-o` = `--output-format` |

- 一つのGoalの継続と、複数タスクのキュー処理を区別する。
- 公式資料の対応であり、現在のユーザーのQwenサーバーでの実行検証はしていない。

## OpenCode

対象: 通常の`opencode` CLI。`opencode2` / v2設定は別扱い

公式: [https://github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)

`opencode.json`の`provider.<id>.options.baseURL`。Chat Completionsなら`@ai-sdk/openai-compatible`。`-m provider/MODEL`で選択。 [opencode-provider](https://opencode.ai/docs/providers/)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `opencode` [opencode-cli](https://opencode.ai/docs/cli/) | — |
| モデル選択 | MIXED | `--model provider/MODEL` / `/models` [opencode-cli](https://opencode.ai/docs/cli/) [opencode-tui](https://opencode.ai/docs/tui/) | `-m` = `--model` |
| 非対話実行 | CLI | `opencode run "PROMPT"` [opencode-cli](https://opencode.ai/docs/cli/) | — |
| 再開 | CLI | `opencode --continue` / `opencode --session ID`。runにも指定可能。 [opencode-cli](https://opencode.ai/docs/cli/) | `-c` = `--continue`<br>`-s` = `--session` |
| 計画 | MIXED | `--agent plan` / TUIでTabによるagent切替 [opencode-agents](https://opencode.ai/docs/agents/) | — |
| 履歴圧縮 | SLASH | `/compact` [opencode-tui](https://opencode.ai/docs/tui/) | `/summarize` = `/compact` |
| 承認制御 | MIXED | `--auto`は明示deny以外を自動承認。`permission`設定で個別制御。 [opencode-cli](https://opencode.ai/docs/cli/) [opencode-permission](https://opencode.ai/docs/permissions/) | — |
| 目標まで継続 | UNVERIFIED | 通常のagent loop。Goalの独立検証付き継続は、本体の今回確認した資料では未確認。 [opencode-agents](https://opencode.ai/docs/agents/) | — |
| テスト・修正 | MODEL | bashでテスト→修正を依頼。formatterとテスト完了ゲートは別。 [opencode-agents](https://opencode.ai/docs/agents/) | — |
| サブエージェント | MIXED | subagentを設定。`@general`等で利用。`opencode agent create`で作成。 [opencode-agents](https://opencode.ai/docs/agents/) [opencode-cli](https://opencode.ai/docs/cli/) | — |
| 定期・背景実行 | CLI | `opencode serve`＋`opencode run --attach URL`。定期起動は外側で管理。 [opencode-cli](https://opencode.ai/docs/cli/) | — |
| 実行上限 | CONFIG | agentの`steps`で推論反復を制限。プロセスの時間上限とは別。 [opencode-agents](https://opencode.ai/docs/agents/) | — |
| 隔離 | UNVERIFIED | permissionは操作許可。OS隔離の汎用フラグはこの資料群で未確認。コンテナ等を外側で用意。 [opencode-permission](https://opencode.ai/docs/permissions/) | — |
| 拡張・MCP | MIXED | `opencode mcp add`、skills、plugins、カスタムコマンド [opencode-cli](https://opencode.ai/docs/cli/) [opencode-tui](https://opencode.ai/docs/tui/) | — |
| 機械可読出力 | CLI | `opencode run --format json "PROMPT"` [opencode-cli](https://opencode.ai/docs/cli/) | — |

- v2は`providers` / `package` / `settings`等の別スキーマ。通常版の`provider` / `npm` / `options`を混ぜない。
- ユーザーが感じた弱さは評価の出発点であり、他ハーネスより劣るという実測結果にはしていない。

## Hermes Agent

対象: Nous Researchの汎用agent。CLI / gateway / Goalは利用面で差がある

公式: [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

`hermes setup`でCustom Endpoint。`model.provider: custom`、`model.base_url: URL`、`model.default: MODEL`。 [hermes-local](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `hermes` / `hermes chat` [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | — |
| モデル選択 | MIXED | `hermes chat --model MODEL` / `/model` [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) [hermes-slash](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/slash-commands.md) | `-m` = `--model` |
| 非対話実行 | CLI | `hermes chat --oneshot --query "PROMPT"`。現行では`-q`単独はTTYで対話を継続する。 [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | `-q` = `--query` |
| 再開 | CLI | `hermes --continue` / `hermes --resume ID` [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | `-c` = `--continue`<br>`-r` = `--resume` |
| 計画 | SLASH | `/plan [TASK]`で計画ファイルを作成 [hermes-slash](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/slash-commands.md) | — |
| 履歴圧縮 | SLASH | `/compress [focus TOPIC]` [hermes-slash](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/slash-commands.md) | — |
| 承認制御 | CLI | `--yolo`で承認をスキップ。通常のapproval設定とは区別。 [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | — |
| 目標まで継続 | SLASH | `/goal OBJECTIVE`、`/goal pause` / `resume`。補助judgeで継続判断。ACPには未実装。 [hermes-goal](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) | — |
| テスト・修正 | SLASH | `/goal gate add COMMAND`。終了コード0を完了の必要条件にできる。通常のjudge判断も続く。 [hermes-goal](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) | — |
| サブエージェント | MIXED | delegate機能。`/bg PROMPT`は別背景セッションで、Goalの自動タスク分割とは別。 [hermes-readme](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/README.md) [hermes-slash](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/slash-commands.md) | — |
| 定期・背景実行 | CLI | `hermes cron create` / `list` / `tick`、`hermes gateway`。複数タスクは`hermes kanban`系。 [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) [hermes-goal](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) | — |
| 実行上限 | MIXED | `--max-turns N`は一会話ターン内のtool反復。Goalは`goals.max_turns`、gateには別のtimeout/retry。 [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) [hermes-goal](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) | — |
| 隔離 | CONFIG | terminal backendにDocker / SSH等を選択。`--worktree`は別のGit分離。 [hermes-readme](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/README.md) [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | — |
| 拡張・MCP | MIXED | skills / MCP / plugins。`/skills`で管理。 [hermes-readme](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/README.md) [hermes-slash](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/slash-commands.md) | — |
| 機械可読出力 | CLI | `hermes -z "PROMPT"`は最終テキスト出力。構造化制御はRPC/SDK面を別途使用。 [hermes-cli](https://github.com/NousResearch/hermes-agent/blob/819988acb750836387fbb9d5d76203a9b3f530f4/website/docs/reference/cli-commands.md) | — |

- GoalとKanbanは別機能。`/goal`だけでボードや並列workerは作られない。
- judgeのデフォルトは主モデル。補助モデル、fallback、外部ツールも確認しないと完全ローカルとは言えない。
- judge単独はLLM判定。テストを必須にする場合はquality gateを併用する。

## DeepSeek Harness (dsh)

対象: 公式developer preview。Web / headless / SDKを区別

公式: [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

WebのSettings → Models → Add a custom provider。`baseURL`とAPI protocolを指定。`llm-pi-ai.providers`で設定可。 [dsh-providers](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/providers.md)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `dsh web`（未導入なら`npx @deepseek-ai/dsh web`） [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | `dsh web` = `dsh --profile web` |
| モデル選択 | UI | Webのモデル選択 / `settings.yaml`。`--model`をlauncherの共通引数とは扱わない。 [dsh-providers](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/providers.md) [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |
| 非対話実行 | CLI | `dsh --profile headless "PROMPT"`。新規永続sessionを作る単発実行。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |
| 再開 | MIXED | Webの既存sessionまたはSDKで復元。共通CLIの`--resume`は資料で未確認。 [dsh-python](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/python-sdk.md) [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |
| 計画 | SLASH | `/plan [PROMPT]` / `/plan off`（command adapterのあるUI） [dsh-plan](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/plan/plan-mode/README.md) | — |
| 履歴圧縮 | UNVERIFIED | compaction subsystemあり。共通CLI／slashの正式な呼出綴りは未確定。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |
| 承認制御 | CONFIG | permission presetで制御。base-backed新規sessionは`workspace-write`。汎用`--yolo`を想定しない。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) [dsh-approval](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/subsystems/permission-presets.md) | — |
| 目標まで継続 | MIXED | `/goal OBJECTIVE` / `pause` / `resume`。Goalサービス＋command＋round-driverの構成に依存。 [dsh-goal](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/goal/command-goal/README.md) [dsh-driver](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/goal/goal-round-driver/README.md) | — |
| テスト・修正 | MODEL | シェルで検証。Goal保存自体には独立した成果検証の保証はない。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) [dsh-driver](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/goal/goal-round-driver/README.md) | — |
| サブエージェント | EXTENSION | subagentプラグイン構成。Codex / Claude委譲は別の任意bundleで、ローカルモデル利用の必須条件ではない。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |
| 定期・背景実行 | UI | Schedule UI／schedule subsystem。配置したprofileと稼働ホストに依存。 [dsh-schedule](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/user/guide/schedule.md) | — |
| 実行上限 | CONFIG | Goalの`maxGoalRounds`（既定256）。round-driverはcap到達等で停止。 [dsh-driver](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/goal/goal-round-driver/README.md) | — |
| 隔離 | CONFIG | sandbox / permission presetを構成。Planモードだけではツールを強制制限しない。 [dsh-plan](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/packages/plan/plan-mode/README.md) [dsh-approval](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/docs/subsystems/permission-presets.md) | — |
| 拡張・MCP | CLI | `dsh plugin --profile NAME add PACKAGE`。MCP clientは同梱、serverは既定で未有効。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |
| 機械可読出力 | CLI | headlessはstdoutに最終文。`dsh --profile sdk`はJSON-RPC、`--profile acp`はACP。 [dsh-cli](https://github.com/deepseek-ai/deepseek-harness/blob/c291e7961a515f6d7af9304e7fd1d257929aef26/apps/cli/reference/README.md) | — |

- Goal状態の永続化と自動再始動は別。session再開／fork後は`/goal resume`等でcontinuationを再度有効にする。
- CLI引数はprofileごとに異なる。`dsh -p`等の他製品由来の省略形を作らない。
- developer previewとして破壊的変更を想定した参照点固定が必要。

## Pi (TypeScript本家)

対象: earendil-works/piのcoding-agent。本家と同名のRust/Python版を混ぜない

公式: [https://github.com/earendil-works/pi](https://github.com/earendil-works/pi)

`~/.pi/agent/models.json`に`baseUrl`、`api: openai-completions`、`apiKey`、`models`を登録。鍵不要サーバーにもダミーkey設定が必要。 [pi-models](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/docs/models.md)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `pi` [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| モデル選択 | MIXED | `--provider PROVIDER --model MODEL` / `/model` [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 非対話実行 | CLI | `pi --print "PROMPT"` [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | `-p` = `--print` |
| 再開 | CLI | `pi --continue`、`pi --resume`でpicker、`pi --session PATH_OR_ID`で指定 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | `-c` = `--continue`<br>`-r` = `--resume` |
| 計画 | EXTENSION | 標準Planモードなし。計画ファイル、extension / packageで追加。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 履歴圧縮 | SLASH | `/compact [PROMPT]`、`/tree`で会話の分岐へ移動 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 承認制御 | NONE | 標準でツール承認popupなし。`--approve`はproject trust用でツール承認とは別。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 目標まで継続 | EXTENSION | 標準Goal機構としては扱わない。RPC / extensionで継続制御を実装。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) [pi-rpc](https://pi.dev/docs/latest/rpc) | — |
| テスト・修正 | MODEL | bashでテスト→修正を依頼。完了ゲートはextension／外部runnerで実装。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| サブエージェント | EXTENSION | 標準subagentなし。extension、package、複数Piプロセスで構成。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 定期・背景実行 | EXTENSION | 標準background bashなし。tmuxや外部schedulerで構成。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 実行上限 | UNVERIFIED | 汎用max-turnsフラグは今回のCLI一覧で未確認。RPCのabortや外部timeoutで補う。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) [pi-rpc](https://pi.dev/docs/latest/rpc) | — |
| 隔離 | EXTENSION | 標準のOS隔離は外部containerまたはextensionで構成。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 拡張・MCP | MIXED | `pi install PACKAGE`。標準MCPなし、extensionで追加。skillsは`/skill:NAME`。 [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) | — |
| 機械可読出力 | CLI | `pi --mode json -p "PROMPT"` / `pi --mode rpc` [pi-readme](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/packages/coding-agent/README.md) [pi-rpc](https://pi.dev/docs/latest/rpc) | — |

- 軽量コアを自分で拡張する用途に向く、という評価は構成からの判断。
- `--yolo`を本家Piの正式フラグとして掲載しない。同名別実装の資料との混同を避ける。
- 会話の`/tree`・forkは、ファイルシステムのGit worktreeを作る操作ではない。

## Aider

対象: CLI。編集・検証中心

公式: [https://github.com/Aider-AI/aider](https://github.com/Aider-AI/aider)

OpenAI互換は`OPENAI_API_BASE=URL`＋`OPENAI_API_KEY=KEY`、`aider --model openai/MODEL`。Ollamaは`ollama_chat/MODEL`。 [aider-models](https://aider.chat/docs/llms.html) [aider-openai](https://aider.chat/docs/llms/openai-compat.html)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `aider` [aider-options](https://aider.chat/docs/config/options.html) | — |
| モデル選択 | MIXED | `--model MODEL` / `/model MODEL` [aider-options](https://aider.chat/docs/config/options.html) [aider-commands](https://aider.chat/docs/usage/commands.html) | — |
| 非対話実行 | CLI | `aider --message "PROMPT"` / `--message-file FILE` [aider-options](https://aider.chat/docs/config/options.html) | `-m` / `--msg` = `--message`<br>`-f` = `--message-file` |
| 再開 | CLI | `--restore-chat-history`。履歴復元であり、停止した任意プロセスを復旧するものではない。 [aider-options](https://aider.chat/docs/config/options.html) | — |
| 計画 | SLASH | `/ask`で相談、`/architect`で設計→editorへ。専用のOS読み取り制限とは別。 [aider-modes](https://aider.chat/docs/usage/modes.html) | — |
| 履歴圧縮 | UNVERIFIED | 自動履歴要約あり。共通`/compact`の存在は今回のcommand一覧で確認できない。 [aider-options](https://aider.chat/docs/config/options.html) [aider-commands](https://aider.chat/docs/usage/commands.html) | — |
| 承認制御 | CLI | `--yes-always`で確認へ自動Yes [aider-options](https://aider.chat/docs/config/options.html) | — |
| 目標まで継続 | EXTENSION | 一依頼の編集と修正。大きい目標のキュー／継続／完了判定は外部runnerで補う。 [aider-options](https://aider.chat/docs/config/options.html) [aider-modes](https://aider.chat/docs/usage/modes.html) | — |
| テスト・修正 | MIXED | `--auto-test --test-cmd COMMAND`、`/test COMMAND`。編集後lintと失敗修正あり。 [aider-test](https://aider.chat/docs/usage/lint-test.html) | — |
| サブエージェント | NONE | Architect / Editorのモデル分離。独立workerへのsubagent委譲とは別。 [aider-modes](https://aider.chat/docs/usage/modes.html) | — |
| 定期・背景実行 | EXTENSION | `--message-file FILE`を外部schedulerから実行 [aider-options](https://aider.chat/docs/config/options.html) | — |
| 実行上限 | CLI | `--max-chat-history-tokens N`は履歴量。壁時計・全作業の反復上限とは別。 [aider-options](https://aider.chat/docs/config/options.html) | — |
| 隔離 | UNVERIFIED | 組み込みOS隔離は今回のoption一覧で未確認。外部container等で構成。 [aider-options](https://aider.chat/docs/config/options.html) | — |
| 拡張・MCP | CLI | `--load FILE`でchat command読込。MCPは今回の標準一覧で未確認。 [aider-options](https://aider.chat/docs/config/options.html) | — |
| 機械可読出力 | CLI | `--chat-history-file FILE` / `--llm-history-file FILE`。汎用JSON event streamとは別。 [aider-options](https://aider.chat/docs/config/options.html) | — |

- `aider -m`はモデル指定ではなくメッセージ。モデルは`--model`を使う。
- 自動テストは合格まで無限に粘る保証ではない。終了後にも外部で成果確認を行える設計にする。

## OpenHands CLI (legacy)

対象: CLIは公式でfeature-complete・安定性維持中心。新しいCanvas/SDKと分離

公式: [https://docs.openhands.dev/openhands/usage/cli/command-reference](https://docs.openhands.dev/openhands/usage/cli/command-reference)

`LLM_MODEL`、`LLM_BASE_URL`、`LLM_API_KEY`＋`--override-with-envs`で既存設定を上書き。 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) [oh-llm](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.llm)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `openhands` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| モデル選択 | MIXED | Settings、または`LLM_MODEL`＋`--override-with-envs` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 非対話実行 | CLI | `openhands --headless --task "PROMPT"` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | `-t` = `--task`<br>`-f` = `--file` |
| 再開 | CLI | `openhands --resume --last` / `openhands --resume ID` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 計画 | UI | command paletteのPlanで計画を見る。専用`/plan`開始コマンドは一覧で未確認。 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 履歴圧縮 | SLASH | `/condense` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 承認制御 | MIXED | `--always-approve`、`--llm-approve`、`/confirm` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 目標まで継続 | UNVERIFIED | 通常agent loop。永続GoalのCLIコマンドは今回の資料で未確認。 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| テスト・修正 | MODEL | agentにテスト実行と失敗修正を依頼 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| サブエージェント | UNVERIFIED | SDKに委譲機能はあるが、このlegacy CLIの利用面で同じ操作を保証しない。 [oh-delegate](https://docs.openhands.dev/sdk/guides/agent-file-based) [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 定期・背景実行 | EXTENSION | headlessを外部schedulerから起動。Canvasのautomation機能とは別。 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) [oh-overview](https://docs.openhands.dev/overview/introduction) | — |
| 実行上限 | UNVERIFIED | このCLI表で全体のmax-turns／壁時計フラグを未確認。SDK設定とは混ぜない。 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 隔離 | CONFIG | workspace / runtime構成に依存。旧`serve`のDocker GUIを新規推奨とはしない。 [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) [oh-overview](https://docs.openhands.dev/overview/introduction) | — |
| 拡張・MCP | MIXED | `openhands mcp add` / `mcp list`、`/skills` [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |
| 機械可読出力 | CLI | `--headless --json`でJSONL [oh-cli](https://docs.openhands.dev/openhands/usage/cli/command-reference) | — |

- 以前の比較から修正: 新規のブラウザ運用はAgent Canvasを確認する。旧Local GUIはdeprecated。
- SDKの機能をそのままCLIの標準コマンド欄へ転記しない。

## OpenHands SDK / Agent Server

対象: 現在のSDK / Agent Server。ブラウザ操作はAgent Canvas

公式: [https://github.com/OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk)

SDKのLLMをローカルproviderへ構成。Canvasはクライアント、推論設定と実行環境は接続先backend側。 [oh-llm](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.llm) [oh-overview](https://docs.openhands.dev/overview/introduction)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | SDK | Python SDKで`Conversation(...)`を作成。CLI表の`openhands`とは別。 [oh-sdk](https://github.com/OpenHands/software-agent-sdk/blob/76e9e25078ed0ff7970f2c75e451274d3ed32bf2/README.md) | — |
| モデル選択 | SDK | `LLM(model=..., base_url=...)`を設定 [oh-llm](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.llm) | — |
| 非対話実行 | SDK | `conversation.send_message(...)` → `conversation.run()` [oh-persist](https://docs.openhands.dev/sdk/guides/convo-persistence) | — |
| 再開 | SDK | 同じ`conversation_id` / `persistence_dir`で復元 [oh-persist](https://docs.openhands.dev/sdk/guides/convo-persistence) | — |
| 計画 | UNVERIFIED | 計画ツール／agent構成による。SDK共通slash commandはない。 [oh-sdk](https://github.com/OpenHands/software-agent-sdk/blob/76e9e25078ed0ff7970f2c75e451274d3ed32bf2/README.md) | — |
| 履歴圧縮 | SDK | condenserの構成。CLIの`/condense`とは別のSDK面。 [oh-condenser](https://docs.openhands.dev/sdk/guides/context-condenser) | — |
| 承認制御 | SDK | confirmation policyを設定。AlwaysConfirm等。 [oh-security](https://docs.openhands.dev/sdk/guides/security) | — |
| 目標まで継続 | SDK | `FINISHED` / `STUCK` / `ERROR`等を監視し、外部controllerで完了判定と再投入を設計。 [oh-api](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.conversation) | — |
| テスト・修正 | SDK | 外部テスト結果をcontrollerの完了条件へ組み込める。実装が必要。 [oh-api](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.conversation) | — |
| サブエージェント | SDK | `DelegateTool` / file-based agent定義 [oh-delegate](https://docs.openhands.dev/sdk/guides/agent-file-based) | — |
| 定期・背景実行 | MIXED | Automation Serverが定期／イベント実行を担当。SDK単体のcronコマンドではない。 [oh-overview](https://docs.openhands.dev/overview/introduction) | — |
| 実行上限 | SDK | Conversationのiteration / stuck設定等を使用。外部プロセス復旧は別途。 [oh-api](https://docs.openhands.dev/sdk/api-reference/openhands.sdk.conversation) | — |
| 隔離 | SDK | Docker等の一時workspace／Agent Serverを構成 [oh-sdk](https://github.com/OpenHands/software-agent-sdk/blob/76e9e25078ed0ff7970f2c75e451274d3ed32bf2/README.md) | — |
| 拡張・MCP | SDK | Python tools / plugins / MCPをagentへ構成 [oh-sdk](https://github.com/OpenHands/software-agent-sdk/blob/76e9e25078ed0ff7970f2c75e451274d3ed32bf2/README.md) [oh-persist](https://docs.openhands.dev/sdk/guides/convo-persistence) | — |
| 機械可読出力 | SDK | Agent ServerのREST / WebSocket、SDKのevents / callbacks [oh-overview](https://docs.openhands.dev/overview/introduction) [oh-persist](https://docs.openhands.dev/sdk/guides/convo-persistence) | — |

- タスクキュー、外部評価、再試行を自分で設計する候補。
- state復元があるだけで、OS再起動後のプロセス自動起動や成功までの無制限再試行が実装済みとは言えない。

## Goose

対象: 旧block/gooseはaaif-goose/gooseへ移転。CLIを対象

公式: [https://github.com/aaif-goose/goose](https://github.com/aaif-goose/goose)

`goose configure`でprovider設定。Ollamaは`OLLAMA_HOST`、OpenAI互換は`OPENAI_HOST`。`--provider` / `--model`で選択。 [goose-provider](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/getting-started/providers.md) [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `goose session` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| モデル選択 | CLI | `--provider PROVIDER --model MODEL` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| 非対話実行 | CLI | `goose run --text "PROMPT"` / `--instructions FILE` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | `-t` = `--text`<br>`-i` = `--instructions` |
| 再開 | CLI | `goose session --resume --session-id ID` / `goose run --resume` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | `-r` = `--resume`（文脈依存） |
| 計画 | SLASH | `/plan [PROMPT]` / `/endplan` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| 履歴圧縮 | SLASH | `/compact` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| 承認制御 | MIXED | `/mode auto` / `approve` / `smart_approve`。`GOOSE_MODE`設定。 [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) [goose-config](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/config-files.md) | — |
| 目標まで継続 | CLI | `goose run --recipe FILE`で定義済み作業。独立したGoal完了検証とは区別。 [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| テスト・修正 | MODEL | recipe／指示にテスト→修正を記載。テスト強制ゲートの有無は別途確認。 [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| サブエージェント | MODEL | 自然言語で並列subagentへ委譲を依頼。専用slash commandではない。 [goose-subagents](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/tutorials/subagents.md) | — |
| 定期・背景実行 | CLI | `goose schedule add` / `list` / `run-now`。schedulerの稼働設定が必要。 [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| 実行上限 | CLI | `goose run --max-turns N` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| 隔離 | UNVERIFIED | 組み込みOS隔離の統一CLIフラグは未確認。Docker Model Runnerは推論backendでありagentの隔離ではない。 [goose-provider](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/getting-started/providers.md) [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |
| 拡張・MCP | MIXED | `goose configure`、`/extension COMMAND`、`/skills`。MCP extensions。 [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) [goose-provider](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/getting-started/providers.md) | — |
| 機械可読出力 | CLI | `goose run --output-format json --text "PROMPT"` / `stream-json` [goose-cli](https://github.com/aaif-goose/goose/blob/50666ae0b9a51e260b52b7efbab2e4e020346e94/documentation/docs/guides/goose-cli-commands.md) | — |

- recipeは作業定義、scheduleは起動条件。成果の正しさの検証と区別する。

## Mistral Vibe

対象: Vibe Code CLI。Webサービスとは別

公式: [https://github.com/mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe)

`~/.vibe/config.toml`の`[[providers]]`に`api_base` / `api_style="openai"` / `backend="generic"`、`[[models]]`にモデルを登録。 [vibe-local](https://docs.mistral.ai/vibe/code/cli/offline-models)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `vibe` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| モデル選択 | MIXED | `--model MODEL` / `/model` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) [vibe-commands](https://docs.mistral.ai/vibe/code/cli/commands-shortcuts) | — |
| 非対話実行 | CLI | `vibe --prompt "PROMPT"` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | `-p` = `--prompt` |
| 再開 | CLI | `vibe --continue` / `vibe --resume ID` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | `-c` = `--continue` |
| 計画 | CLI | `vibe --agent plan` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| 履歴圧縮 | SLASH | `/compact [INSTRUCTIONS]` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| 承認制御 | CLI | `--auto-approve` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | `--yolo` = `--auto-approve` |
| 目標まで継続 | UNVERIFIED | 通常agent loop。独立Goal検証の標準コマンドは今回の資料で未確認。 [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| テスト・修正 | MODEL | shellでテスト→修正を依頼 [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| サブエージェント | CONFIG | 組み込みexplore等のsubagent／カスタムagentを構成 [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| 定期・背景実行 | EXTENSION | `--prompt`で外部schedulerから起動。`/teleport`はクラウド移送でローカル定期実行ではない。 [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) [vibe-commands](https://docs.mistral.ai/vibe/code/cli/commands-shortcuts) | — |
| 実行上限 | CLI | `--max-turns N` / `--max-tokens N` / `--max-price N` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| 隔離 | UNVERIFIED | `--worktree NAME`はGit分離。OS隔離の標準設定は今回の資料で確定しない。 [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |
| 拡張・MCP | MIXED | skills / MCP、`/reload`。設定は`config.toml`。 [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) [vibe-commands](https://docs.mistral.ai/vibe/code/cli/commands-shortcuts) | — |
| 機械可読出力 | CLI | `vibe -p "PROMPT" --output json` [vibe-readme](https://github.com/mistralai/mistral-vibe/blob/19b5b74faa78d0816b8d4d4c7d7543fc3520678c/README.md) | — |

- 完全オフライン目的ではtelemetry / auto update / 外部MCP・connectorも別途設定する。
- 価格上限はローカル推論の計算時間上限ではない。

## Kilo Code CLI

対象: 現行`kilo` CLI。古いCLI／VS CodeのUI手順を混ぜない

公式: [https://github.com/Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode)

`kilo.jsonc`のproviderにローカルendpointとMODELを設定。Ollama / LM Studio / Atomic Chatを公式案内。 [kilo-local](https://kilo.ai/docs/automate/extending/local-models) [kilo-models](https://kilo.ai/docs/code-with-ai/agents/custom-models)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `kilo` [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | — |
| モデル選択 | MIXED | `--model provider/MODEL` / `/models` [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | `-m` = `--model` |
| 非対話実行 | CLI | `kilo run "PROMPT"` [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | — |
| 再開 | MIXED | `kilo run --continue "PROMPT"` / `--session ID`、`/sessions` [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | `-c` = `--continue`<br>`-s` = `--session`<br>`/resume` / `/continue` = `/sessions` |
| 計画 | MIXED | `--agent NAME` / `/agents`で計画用agentを選択。導入済みagent名を確認。 [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | — |
| 履歴圧縮 | SLASH | `/compact` [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | `/summarize` = `/compact` |
| 承認制御 | CLI | `kilo run --auto "PROMPT"`。明示denyは残る。 [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | — |
| 目標まで継続 | UNVERIFIED | 通常agent loop／Orchestrator。独立したGoal完了検証の標準コマンドは未確認。 [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | — |
| テスト・修正 | MODEL | テスト実行・修正をagentへ依頼 [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | — |
| サブエージェント | MIXED | Orchestrator / custom agents。`kilo agent`で管理。 [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | — |
| 定期・背景実行 | CLI | `kilo serve` / `kilo daemon`。定期タスクの実行は別途構成。 [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | — |
| 実行上限 | UNVERIFIED | 汎用の全実行時間フラグは今回のCLI表では未確定。外側で管理。 [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | — |
| 隔離 | UNVERIFIED | 承認設定とOS隔離を別扱い。今回の資料で統一sandboxフラグ未確認。 [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | — |
| 拡張・MCP | CLI | `kilo mcp` / `kilo plugin MODULE`、skills [kilo-commands](https://kilo.ai/docs/code-with-ai/platforms/cli) | — |
| 機械可読出力 | CLI | `kilo run --format json "PROMPT"` [kilo-cli](https://kilo.ai/docs/code-with-ai/platforms/cli-reference) | — |

- `kilo run -p`はpassword。プロンプトは位置引数。
- CLIの`kilo console`は公式にdeprecatedと案内されている。

## Cline CLI

対象: 現行apps/cliを対象。旧CLIの引数との混在に注意

公式: [https://github.com/cline/cline](https://github.com/cline/cline)

`cline auth`でprovider / base URLを設定、`--provider` / `--model`で選択。ローカルprovider対応あり。 [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) [cline-local](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/running-models-locally/overview.mdx)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `cline` / `cline --tui` [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) | `-i` = `--tui` |
| モデル選択 | CLI | `--provider PROVIDER --model MODEL` [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) | `-P` = `--provider`<br>`-m` = `--model` |
| 非対話実行 | CLI | `cline --json "PROMPT"`。`--yolo`実行もターン完了で終了。 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| 再開 | CLI | `cline --id ID`。一覧は`cline history`。 [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) | `cline h` = `cline history` |
| 計画 | CLI | `cline --plan "PROMPT"` [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) | `-p` = `--plan` |
| 履歴圧縮 | CLI | `--compaction agentic` / `basic` / `off`。手動slashとは別。 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| 承認制御 | CLI | `--auto-approve true` / `--yolo`。yoloはspawn/teamを既定で無効化する。 [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | `-y` = `--yolo` |
| 目標まで継続 | UNVERIFIED | 単発終了・background hubあり。独立Goal判定の正式コマンドは今回の資料で未確認。 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| テスト・修正 | MODEL | ツールでテスト→修正を依頼 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| サブエージェント | MIXED | spawn/team機能あり。ただしyolo/zenでは既定無効。 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| 定期・背景実行 | CLI | `cline schedule create`、`cline --zen "PROMPT"`はhubへ背景投入。 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | `-z` = `--zen` |
| 実行上限 | CLI | `--timeout SECONDS` / `--retries N`。retriesは連続mistake上限。 [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) | `-t` = `--timeout` |
| 隔離 | CLI | `--data-dir PATH`で状態分離／sandbox mode。ただしOSレベルの隔離保証は別途確認。 [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| 拡張・MCP | CLI | `cline mcp` / `cline plugin`、hooks / skills [cline-cli](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/docs/cli/cli-reference.mdx) [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |
| 機械可読出力 | CLI | `--json`でNDJSON / `--acp` [cline-readme](https://github.com/cline/cline/blob/cfe9cadab99617d5013bf89f07b079d105057791/apps/cli/README.md) | — |

- `-p`はpromptではなくplan、`-c`はcontinueではなくcwd。
- 公式CLI referenceとREADMEでdefault値に差があるため、既定のauto approval / compaction値は断定しない。
- hubに投入してCLIが終了したことは、タスク成功を意味しない。

## Gemini CLI

対象: Google公式CLI。本体を改造したforkやQwen Codeとは別

公式: [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

公式認証・設定資料では、任意のローカルQwen Chat Completionsサーバーへ直接つなぐ標準経路を確認できなかった。不可能という断定ではない。 [gemini-auth](https://geminicli.com/docs/get-started/authentication/) [gemini-config](https://geminicli.com/docs/reference/configuration/)

| 機能 | 操作種別 | 正式コマンド／機能 | 公式の短縮形・別名 |
| --- | --- | --- | --- |
| 起動 | CLI | `gemini` [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) | — |
| モデル選択 | CLI | `--model MODEL`。モデル名指定だけで任意ローカルproviderへ変わるわけではない。 [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) [gemini-auth](https://geminicli.com/docs/get-started/authentication/) | `-m` = `--model` |
| 非対話実行 | CLI | `gemini --prompt "PROMPT"` [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) | `-p` = `--prompt` |
| 再開 | CLI | `gemini --resume latest` / `--resume ID` [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) [gemini-config](https://geminicli.com/docs/reference/configuration/) | `-r` = `--resume` |
| 計画 | CLI | `--approval-mode plan`。headlessでは実装へ自動遷移する挙動あり。 [gemini-plan](https://geminicli.com/docs/cli/plan-mode/) | — |
| 履歴圧縮 | SLASH | `/compress` [gemini-commands](https://geminicli.com/docs/reference/commands/) | — |
| 承認制御 | CLI | `--approval-mode yolo`。古い`--yolo`はcheatsheetでdeprecated。 [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) | — |
| 目標まで継続 | UNVERIFIED | ローカルLLMでの自律Goalは未検証。通常のheadless agent loopとは区別。 [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) [gemini-auth](https://geminicli.com/docs/get-started/authentication/) | — |
| テスト・修正 | MODEL | シェルでテスト→修正を依頼。ローカルQwen対応を意味しない。 [gemini-config](https://geminicli.com/docs/reference/configuration/) | — |
| サブエージェント | SLASH | `/agents list` / `/agents reload`等でsubagentを管理。ローカルQwen接続は未確認。 [gemini-commands](https://geminicli.com/docs/reference/commands/) | `/agents refresh` = `/agents reload` |
| 定期・背景実行 | EXTENSION | headlessを外部schedulerで起動する構成 [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) | — |
| 実行上限 | CONFIG | `model.maxSessionTurns`等の設定。導入版のschemaを確認。 [gemini-config](https://geminicli.com/docs/reference/configuration/) | — |
| 隔離 | CLI | `--sandbox` [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) | `-s` = `--sandbox` |
| 拡張・MCP | CONFIG | extensions / MCP / skills / hooks [gemini-config](https://geminicli.com/docs/reference/configuration/) | — |
| 機械可読出力 | CLI | `--output-format json` / `stream-json` [gemini-cli](https://geminicli.com/docs/cli/cli-reference/) | `-o` = `--output-format` |

- Gemini CLIとそのforkであるQwen Codeのprovider対応を混同しない。
- ローカル接続を必須条件にした候補選びでは保留。
