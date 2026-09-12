# 既存のローカルサーバーへ接続する例

**未実行の設定テンプレート**です。`MODEL_ID`をサーバーが公開する正確なIDへ、`8080`を実際のポートへ置換します。既存ファイルを丸ごと上書きせず、必要な項目を統合してください。サーバーを新しく起動する手順は含めません。

ここではChat Completions互換endpointを`http://127.0.0.1:8080/v1`と仮定しています。認証が有効なら`local-not-a-secret`を実際の鍵の環境変数参照へ変更します。**`127.0.0.1`はCLIの実行場所から見たアドレス**なので、agentを別コンテナに入れる場合は到達できるアドレスに置き換えます。

## Qwen Code

```bash
qwen --auth-type openai \
  --openai-base-url http://127.0.0.1:8080/v1 \
  --openai-api-key local-not-a-secret \
  --model MODEL_ID
```

Goalを非対話実行する例（テスト内容は対象プロジェクトに合わせる）:

```bash
qwen --auth-type openai \
  --openai-base-url http://127.0.0.1:8080/v1 \
  --openai-api-key local-not-a-secret \
  --model MODEL_ID \
  --max-wall-time 1h --max-session-turns 100 \
  -p '/goal TASK.mdの目標と完了条件を満たす'
```

これは承認ポリシーを自動変更しません。無人運用では実行環境に合わせて承認・sandboxを別途設定します。[provider仕様](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/)・[Headless](https://qwenlm.github.io/qwen-code-docs/en/users/features/headless/)

## Hermes

`~/.hermes/config.yaml`の該当部分:

```yaml
model:
  provider: custom
  base_url: http://127.0.0.1:8080/v1
  default: MODEL_ID
goals:
  max_turns: 20
```

認証情報は`hermes setup`のCustom Endpointから設定できます。Goalは対話画面で設定します。以下はシェルコマンドではありません。

```text
/goal TASK.mdの目標を満たす
/goal gate add python3 -m pytest tests
/goal status
```

`pytest`はテストコマンドの一例です。gateはテストを成功させるまでの無制限実行ではなく、retry / timeout上限があります。[ローカル接続](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)・[Goal / gate](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)

## Grok Build

`~/.grok/config.toml`へカスタムモデルを追加する例:

```toml
[model.local-qwen]
model = "MODEL_ID"
name = "Local Qwen"
base_url = "http://127.0.0.1:8080/v1"
api_backend = "chat_completions"
env_key = "LOCAL_LLM_API_KEY"
supports_backend_search = false
supports_reasoning_effort = false
```

```bash
LOCAL_LLM_API_KEY=local-not-a-secret grok --model local-qwen
```

`supports_reasoning_effort`等は実際のサーバー能力に合わせます。補助モデル設定も別途確認します。[公式設定](https://docs.x.ai/build/settings/reference)

## DeepSeek Harness

`dsh web`を起動し、**Settings → Models → Add a custom provider**で次を設定します。

| 設定 | 値の例 |
| --- | --- |
| Provider ID | `local-qwen` |
| Base URL | `http://127.0.0.1:8080/v1` |
| API protocol | `openai-completions` |
| Credential | サーバーの認証設定に合わせる |
| Model ID | `MODEL_ID` |

選択後、command adapterのあるWeb画面で`/goal OBJECTIVE`を使用します。`dsh --profile headless`の位置引数にslash commandを渡せばUIと同じように処理される、と仮定しないでください。[公式providers](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/providers.md)・[CLI](https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/reference/README.md)

## Pi

`~/.pi/agent/models.json`へproviderを追加:

```json
{
  "providers": {
    "local-qwen": {
      "baseUrl": "http://127.0.0.1:8080/v1",
      "api": "openai-completions",
      "apiKey": "local-not-a-secret",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [{"id": "MODEL_ID"}]
    }
  }
}
```

```bash
pi --provider local-qwen --model MODEL_ID
```

context上限・出力上限は実際のサーバーに合わせて追加します。`compat`もサーバー次第です。[本家models仕様](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md)

## OpenCode（通常版）

`opencode.json`への追加例:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "local-qwen/MODEL_ID",
  "provider": {
    "local-qwen": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:8080/v1",
        "apiKey": "local-not-a-secret"
      },
      "models": {"MODEL_ID": {"name": "Local Qwen"}}
    }
  }
}
```

これは`opencode2`のスキーマではありません。[通常版provider](https://opencode.ai/docs/providers/)

## Aider

```bash
OPENAI_API_BASE=http://127.0.0.1:8080/v1 \
OPENAI_API_KEY=local-not-a-secret \
aider --model openai/MODEL_ID
```

編集後の検証を加える場合は、例えば`--auto-test --test-cmd 'python3 -m pytest tests'`を指定します。[互換API](https://aider.chat/docs/llms/openai-compat.html)・[テスト](https://aider.chat/docs/usage/lint-test.html)

## Mistral Vibe

`~/.vibe/config.toml`のprovider / model定義例:

```toml
[[providers]]
name = "local-qwen"
api_base = "http://127.0.0.1:8080/v1"
api_style = "openai"
backend = "generic"

[[models]]
name = "MODEL_ID"
provider = "local-qwen"
alias = "local-qwen"
```

起動後に`/model`または`/config`から選択します。[公式offline models](https://docs.mistral.ai/vibe/code/cli/offline-models)

## Codex / Claude CodeのAPI差

| ハーネス | 接続例 | 条件 |
| --- | --- | --- |
| Codex | `codex --oss --local-provider ollama --model MODEL_ID` | 導入したproviderが必要なResponses APIを提供すること |
| Claude Code | 下記環境変数で`claude --model MODEL_ID` | Anthropic Messages互換API。ここではOllamaの例 |

```bash
ANTHROPIC_AUTH_TOKEN=ollama \
ANTHROPIC_API_KEY='' \
ANTHROPIC_BASE_URL=http://127.0.0.1:11434 \
claude --model MODEL_ID
```

Chat Completionsサーバーが動いているというだけで、この2つも同じURL指定で動くとは限りません。[Codex CLI](https://learn.chatgpt.com/docs/developer-commands?surface=cli)・[Codex provider](https://learn.chatgpt.com/docs/config-file/config-reference)・[Ollama / Claude Code](https://docs.ollama.com/integrations/claude-code)

Goose、Kilo、Cline、OpenHandsは[ローカル対応表](../docs/local-models.md)に設定入口と一次資料をまとめています。Gemini CLIは任意のQwen endpointへ接続する標準経路を未確認のため、動作するかのような設定例を掲載していません。
