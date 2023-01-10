# 仕様

これは実行可能な仕様ファイルです。
このファイルはマークダウン構文に従います。
このファイルの各見出しは、シナリオを示しています。
すべての箇条書きはステップを示します。

この仕様ファイルの実行方法
```sh
> gauge run specs
```

シナリオの外にもステップを書けます。

* 英語の母音とは "aeiou" である

## 母音の数（1つの単語）

tags: single word

* "gauge" の母音の数は "3" であること
* "test" の母音の数は "1" であること

## 母音の数（複数の単語）

これは、この仕様の2つ目のシナリオです。
テーブル駆動形式のシナリオです。

* 下記テーブルに示すように、ほぼすべての単語に母音が含まれること

   |Word  |Vowel Count|
   |------|-----------|
   |Gauge |3          |
   |Mingle|2          |
   |Snap  |1          |
   |GoCD  |1          |
   |Rhythm|0          |
