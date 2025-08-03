# DiscordAITestBot

## Requirements
- Python3
- pip
- discord
- google-genai

## Catch Discord post format
```
📣 成果物（アウトプット）のコミットがありました！
👤 ユーザー: USER_NAME
📝 メッセージ: COMMIT_MESSAGE
🔗 https://github.com/USER_NAME/REPOSITORY_NAME/commits/BRANCH_NAME
```

## Bot post format
```
USER_NAMEさん、REPOSITORY_NAMEのリポジトリを拝見しました。

最新のコミットの内容から、Javaの基本的な制御構造（if文、for文）やデータ型、そしてクラスの概念を理解されていることが伺えます。特に、newキーワードを使ったオブジェクトの生成やメソッド呼び出しの部分は、オブジェクト指向プログラミングの基礎が身についていることを示しています。

また、変数のスコープ（ローカル変数とインスタンス変数）に関する理解も見られ、プログラミングにおける良い習慣を身につけようとされている印象を受けました。まだ入門段階ではありますが、着実にJavaの基礎を固められていると感じます。

それでは、これまでの学習内容をさらに深め、次に進むための技術クイズを3問作成しました。頑張ってください！

---

Q1: 以下のJavaコードを実行した際に出力される内容として正しいものを選択してください。

public class ScopeTest {
    int instanceVar = 10;

    public void printNumbers() {
        int localVar = 20;
        System.out.println("Instance Var: " + instanceVar);
        System.out.println("Local Var: " + localVar);
    }

    public static void main(String[] args) {
        ScopeTest st = new ScopeTest();
        st.printNumbers();
    }
}


A.
Instance Var: 10
Local Var: 20

B.
Instance Var: 0
Local Var: 20

C.
Instance Var: 10
Local Var: 0

D.
コンパイルエラーが発生する

Q2: 以下のJavaコードには誤りがあり、コンパイルエラーが発生します。このコードが意図通りに「Hello, Java!」と出力されるように修正する際、最も適切な変更はどれでしょうか？

public class LoopExample {
    public static void main(String[] args) {
        for (int i = 0; i <= 5; i++) {
            if (i == 3) {
                System.out.println("Hello, Java!");
            }
        }
    }
}


A. for (int i = 0; i <= 5; i++) を for (int i = 0; i < 5; i++) に変更する。
B. if (i == 3) を if (i = 3) に変更する。
C. System.out.println("Hello, Java!"); の行を for ループの外に移動する。
D. コードは正しく、コンパイルエラーは発生しない。

Q3: Javaにおけるクラスとオブジェクトの関係について、以下の説明のうち正しいものはどれですか？

A. クラスは具体的な「もの」そのものであり、オブジェクトはクラスを定義するための設計図である。
B. クラスは「設計図」のようなものであり、オブジェクトはその設計図に基づいて作られた具体的な「実体」である。
C. オブジェクトはクラスのメソッドを定義する場所であり、クラスはオブジェクトをインスタンス化する場所である。
D. クラスとオブジェクトは同じ意味で使われることが多く、厳密な違いはない。
```
