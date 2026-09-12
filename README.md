# ローカルLLM向けハーネス比較

**確認日: 2026-09-13（JST）**。ローカルQwenなどの推論サーバーを使い、実装・検証を自律的に進めるハーネスを比較する日本語リポジトリです。

15製品・16実行面について、ローカルLLMへの接続経路と、15機能のコマンド対応・正式エイリアスを整理しています。**ドキュメント／ソースの確認であり、同一モデルでの完走率ベンチマークではありません。** コマンドや設定例は掲載のみで、ハーネスのインストール、推論実行、既存設定の変更はしていません。

## 比較表

| 読みたい内容 | ファイル |
| --- | --- |
| ローカルLLMが使えるか・API形式・接続設定 | [ローカル対応表](docs/local-models.md) |
| 起動・モデル・非対話・再開・計画・圧縮・承認・JSON出力 | [コマンド比較表](docs/commands.md) |
| Goal継続・テスト・上限・委譲・定期実行・隔離・拡張 | [自律運用比較表](docs/autonomy.md) |
| 機能ごとの正式な短縮形／エイリアスと製品別注意点 | [個別詳細](docs/details.md) |
| 同じ短縮オプションの意味の違い | [エイリアスの読み方](docs/aliases.md) |
| Qwenなどの既存サーバーにつなぐ設定例 | [ローカル設定例](examples/local-configs.md) |
| 放置運用で比較するタスク・完了条件 | [評価手順](docs/evaluation.md) |
| 一次資料と取得記録 | [出典台帳](docs/sources.md) |
| 機械処理 | [JSON](data/harnesses.json)・[コマンドCSV](data/commands.csv)・[ローカル対応CSV](data/local-models.csv) |

## 対象

Codex CLI、Claude Code、Grok Build、Qwen Code、OpenCode、Hermes Agent、DeepSeek Harness、Pi、Aider、OpenHands CLI、OpenHands SDK / Agent Server、Goose、Mistral Vibe、Kilo Code CLI、Cline CLI、Gemini CLI。

OpenHandsは同一製品群の異なる実行面を2行にしています。Grokは公式`grok` CLI（Grok Build）、DeepSeekは公式`deepseek-ai/deepseek-harness`、Piは`earendil-works/pi`のTypeScript版を対象にしています。

これは指定された製品と代表的な周辺候補を調べたスナップショットです。世界中のハーネス、同名fork、IDE専用製品を完全に網羅するものではありません。Cursor、Copilot、OpenClaw、各種Ralph wrapper等の未掲載製品を「ローカル非対応」と判断しているわけではありません。

## 放置運用で見るポイント

機能構成からの候補の絞り方です。性能順位ではありません。

| 用途 | 検討候補 | 理由・条件 |
| --- | --- | --- |
| 目標を渡し、テスト成功を完了条件にして継続 | Hermes | `/goal`とquality gate。補助judgeと実行上限を設定する。[仕様](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) |
| CLIからGoal付きの非対話実行を始める | Qwen Code | HeadlessでGoal作成・再開が可能。[仕様](https://qwenlm.github.io/qwen-code-docs/en/users/features/headless/) |
| Web UIとプラグイン構成でGoalを制御 | DeepSeek Harness | Goal commandとround-driverを構成。developer preview。[公式](https://deepseek.com/harness/en/) |
| タスクキュー・外部評価・復旧を自分で設計 | OpenHands SDK / Agent Server | 会話状態を保存し、実行状態を監視できる。[永続化](https://docs.openhands.dev/sdk/guides/convo-persistence) |
| 軽いコアに独自の継続制御を載せる | Pi | 標準機能を絞りextension / RPCで拡張する設計。[本家](https://pi.dev/docs/latest) |
| 対象ファイルとテストを指定して修正させる | Aider | 編集後の自動lint・testを設定できる。[検証](https://aider.chat/docs/usage/lint-test.html) |

Codex・Claude Codeは比較の基準として含めています。ユーザーの用途ではこれらを本人用に残し、別のハーネスをローカルLLM用に選ぶ前提です。

## 表の読み方

- **対応経路あり**: 一次資料にローカル／任意endpointの設定がある。任意のモデルでの成功を保証しない。
- **条件付き**: 必要なAPI互換層などを満たせば接続経路がある。例: Claude CodeのAnthropic Messages互換。
- **公式経路未確認**: 読んだ資料で確認できなかった。「技術的に不可能」「非対応」とは断定しない。
- **CLI / SLASH / CONFIG / SDK / EXTENSION / MODEL / UI**: 呼び出す場所。`MODEL`は自然言語でモデルに依頼する処理で、決定的なハーネス制御ではない。
- **NONE**: 当該の標準機能がないことを資料が明示、または別概念であることを明記。**UNVERIFIED**は確認不足。
- **MIXED**: CLIとUI、設定とtoolなど複数の操作面を含む。
- `PROMPT`、`MODEL`、`ID`、`URL`、`KEY`は置換用。表中のスラッシュコマンドを、そのままシェルで実行しない。

「正式エイリアス」は上流が同義と定義している別名です。機能対応表の同じ列に並んだ他製品のコマンドとは、同一の挙動を保証しません。

## 混同しやすい境界

1. **ローカル推論と完全オフライン**: 主モデルがローカルでも、要約・judge・embedding・fallback・検索・MCPが外部へ接続する場合がある。
2. **API互換性**: Chat Completions、Responses、Anthropic Messagesは別。`base_url`だけ変えて接続できるとは限らない。
3. **非対話実行と継続**: 一回のagent loop、Goalの自動再投入、定期起動、複数タスクのキューは別機能。
4. **状態保存と復旧**: セッションを復元できても、OS再起動後にプロセスが勝手に再開するとは限らない。
5. **完了宣言と検証**: モデル／judgeの「完了」と、固定したテストの終了コードを別々に確認する。
6. **承認と隔離**: 全自動承認、OS sandbox、Git worktree、会話forkは別の機構。

OpenHandsの現在の構成はAgent Canvas / SDK / Agent Server等へ分かれています。旧CLIは安定性維持中心、旧Local GUIはdeprecatedなので、以前の一括したOpenHands比較よりも対象を分けています。[公式構成図](https://docs.openhands.dev/overview/introduction)

OpenCodeには通常版とv2のドキュメントがあり、provider設定のキーが違います。本表は通常の`opencode`を対象とし、v2の設定を混ぜていません。[通常版](https://opencode.ai/docs/providers/)・[v2](https://opencode.ai/v2/docs/providers)

## 更新・検証

Python 3の標準ライブラリのみで表を再生成できます。

```bash
python3 scripts/render.py
python3 scripts/render.py --check
```

一次資料を再取得し、URL・HTTP状態・本文hashを記録する場合:

```bash
python3 scripts/audit_sources.py
```

`audit_sources.py`は接続可否・内容の変化を記録するだけで、本文の主張やコマンドの正しさを自動証明しません。変更時は資料を読み直し、`data/harnesses.json`の根拠と確認日を更新します。

GitHub出典は可能な限り確認時のコミットへ固定しています。`data/upstream-revisions.json`のSHAはdefault branchの参照点で、最新安定リリースや動作保証済み版を意味しません。実機確認したのはCodex CLI 0.154.0の`--help` / `--version`のみです。

## リポジトリの構成

```text
README.md
data/
  harnesses.json            # 手でレビューする正本
  commands.csv              # 自動生成
  local-models.csv          # 自動生成
  upstream-revisions.json   # 上流参照点
  source-audit.json         # URL取得結果・hash
docs/
  local-models.md           # 自動生成
  commands.md               # 自動生成
  autonomy.md               # 自動生成
  details.md                # 自動生成
  sources.md                # 自動生成
  aliases.md
  evaluation.md
examples/
  local-configs.md
scripts/
  render.py
  audit_sources.py
```
