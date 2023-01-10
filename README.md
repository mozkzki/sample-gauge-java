# sample-gauge-java

gaugeのサンプル(ステップ実装言語はJava)

## 詳細

- gaugeのVSCodeプラグインを入れて「Create a new Gauge Project」でテンプレート作成
- `example.spec`と`StepImplementation.java`を日本語化

### 実行方法

```sh
gauge run specs
```

もしくはspecファイルの「Run Spec」や「Run Scenario」をクリックしても良い

### レポート

実行するとローカルに`reports/html-report/index.html`が出力されるのでブラウザで見る

### GitHub Actions 連携

GitHub Actionsでのテスト実施、テストレポート公開(GitHub Pages)まで実施

- `reports/html-report`フォルダをPagesに公開している
- URLは下記になる
  - <https://mozkzki.github.io/sample-gauge-java/specs/example.html>
- GitHub側でPagesを有効化（Source: GitHub Actions）する必要あり

## 参考

- [簡単！自動化テストツール「Gauge」の導入からテスト実行まで ｜SHIFT Group 技術ブログ｜note](https://note.com/shift_tech/n/n8cfe237382a4)
- [Selenium練習サイトを使って、Gherkin vs Gaugeしてみた - Qiita](https://qiita.com/KazuhiroYoshino/items/876f59ce3b8c547ea8f9)
- [Gauge Documentation](https://docs.gauge.org/writing-specifications.html?os=macos&language=java&ide=vscode)
- [実践ATDD 〜TDDから更に歩みを進めたソフトウェア開発へ〜 / ATDD by genba example - Speaker Deck](https://speakerdeck.com/hgsgtk/atdd-by-genba-example)
- [カスタムワークフローで GitHub Pages デプロイが可能に | 豆蔵デベロッパーサイト](https://developer.mamezou-tech.com/blogs/2022/09/08/github-pages-new-deploy-method/)
