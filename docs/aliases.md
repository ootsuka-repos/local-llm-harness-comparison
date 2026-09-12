# コマンド対応とエイリアス

確認日: 2026-09-13。[機能対応表](commands.md)と[製品別の正式エイリアス](details.md)を併用してください。

## 同じ短縮形でも意味が違う

| オプション | 製品・意味 | 対照 |
| --- | --- | --- |
| `-p` | Claude Code / Qwen Code / Pi / Vibe / Gemini: 非対話プロンプト系 | Codex: profile、Cline: plan、Kilo run / OpenCode attach: password |
| `-m` | 多くのCLI: model | Aider: message。Aiderのモデルは`--model` |
| `-c` | 多くのCLI: continue | Cline: cwd。Codex: config override |
| `-s` | Codex / Gemini: sandbox | Hermes: skills、OpenCode / Kilo: session |
| JSONストリーム | Claude / Qwen / Gemini: `stream-json` | Grok: `streaming-json`、OpenCode / Kilo: `--format json`、Pi: `--mode json`、Cline: `--json` |

根拠: [Codex](https://learn.chatgpt.com/docs/developer-commands?surface=cli)、[Claude](https://code.claude.com/docs/en/cli-reference)、[Qwen](https://qwenlm.github.io/qwen-code-docs/en/users/features/headless/)、[Aider](https://aider.chat/docs/config/options.html)、[Grok](https://docs.x.ai/build/cli/headless-scripting)、その他は[出典台帳](sources.md)の各CLI資料。

## ユーザー定義のシェル別名を作る場合

以下は**この比較のための独自例**であり、公式エイリアスではありません。事前に各ハーネスのローカルproviderを設定して使います。全許可・sandbox無効化は別名に埋め込んでいません。

```bash
# 必要な行だけ、自分のshellで定義する例。自動登録はしていません。
alias h-codex='codex'
alias h-claude='claude'
alias h-grok='grok'
alias h-qwen='qwen'
alias h-opencode='opencode'
alias h-hermes='hermes'
alias h-dsh='dsh web'
alias h-pi='pi'
alias h-aider='aider'
alias h-goose='goose session'
alias h-vibe='vibe'
alias h-kilo='kilo'
alias h-cline='cline'
```

これらは起動名を短くするだけです。プロンプト指定、再開、承認、JSON形式まで一括で統一するwrapperにはしていません。例えば`h-cline -p`は依然として計画モードです。

## 放置運用の操作を分ける

| 操作 | 意味 | 例 |
| --- | --- | --- |
| Run | 一つの依頼をagent loopへ投入 | `qwen -p "PROMPT"` |
| Goal | 未完了なら次のターンを自動で進める | Qwen / Hermes / dshの`/goal`。各製品で実行面と判定方式が異なる |
| Resume | 保存した会話／状態を復元 | `pi --continue`。それだけでプロセス復旧の常駐監視にはならない |
| Schedule | 時刻やイベントで作業を起動 | `hermes cron` / `goose schedule` |
| Queue / Board | 複数タスクの順序・担当・依存を管理 | Hermes Kanban。単一Goalとは別 |
| Gate | 決定的なコマンド成功を完了の必要条件にする | Hermesの`/goal gate add COMMAND` |

根拠: [Qwen Headless](https://qwenlm.github.io/qwen-code-docs/en/users/features/headless/)、[Hermes Goal / Kanban / gates](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)。
