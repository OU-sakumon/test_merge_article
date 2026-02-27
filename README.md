# 部誌統合テスト

## 流れ（記事の編集から公開まで）

1. **最新の状態を取得**  
   以下のコマンドを実行して最新状態にしてください。
   ```bash
   git checkout main
   git pull origin main
   ```

2. **ブランチの作成**  
   `git checkout -b <名前と記事>` でブランチを作成します。  
   例: `git checkout -b tanakamikihisa_vector`

3. **記事の編集**  
   これ以降、記事の編集は作成したブランチ内で行ってください。  
   自分の記事フォルダ以外は触らないでください。
   まず、`template`フォルダにある`temp`フォルダをこのまま`articles`フォルダにコピペしてください。
   そして、コピペした`temp`フォルダを`<作ったブランチ名>`に変更してください。
   記事の編集では、このフォルダのファイル名、フォルダ名は変更しないでください。

4. **記事の提出**  
   以下のコマンドを**順番に**実行して記事を提出してください。
   ```bash
   git pull origin main
   git add articles/<自分の記事フォルダ名>/
   git commit -m "<コメント>"
   git push origin <作成したブランチ名>
   ```

5. **Pull Request の作成**  
   4 の後に、GitHub 上で Pull Request を作成してください。

6. **管理者による merge**  
   管理者は届いた Pull Request を確認し、merge を行ってください。

7. **PDF の自動生成**  
   main に merge されると、GitHub Actions で統合 PDF（main.pdf）がビルドされ、Artifacts に保存されます（30日間）。Run 完了後、Actions タブからダウンロードできます。

---

## ローカルでビルドする場合
  プロジェクトルートで以下を実行してください。
  ```bash
  make
  ```

- **記事単体のみビルド**  
  対象の記事フォルダに移動してから実行してください。
  ```bash
  cd articles/<記事フォルダ名>
  make pdf
  ```
  その記事の `main.pdf` が同じフォルダ内に生成されます。