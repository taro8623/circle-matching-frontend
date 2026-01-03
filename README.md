## 🧩 設計メモ

### ■ アカウント仕様
- ユーザーアカウントは 1 つで複数サークルに参加可能
- サークルごとに「サークル内表示名」を設定できる
- サークル内表示名が未入力の場合は共通ユーザー名を使用する

### ■ UI / フロントエンド方針
- まずは画面の骨組み（Signup / Login / Register など）を作成
- 画面遷移とフォーム入力が動く状態を優先
- デザインは後回しで OK
- API 接続は UI が揃ってから順次実装する

### ■ バックエンド方針（FastAPI）
- `/signup` `/login` の API を先に作成し、フロントと接続
- DB（SQLite）を後から接続し、ユーザー情報を保存
- パスワードはハッシュ化して保存する
- 認証は JWT を使用予定

---

## 📌 タスク進捗状況

### ✅ 完了済み
- [x] React プロジェクト作成（Vite）
- [x] ルーティング設定（/signup /login /register）
- [x] Signup 画面のフォーム作成
- [x] Login 画面のフォーム作成
- [x] Signup / Login の fetch 実装（フロント → FastAPI）
- [x] FastAPI プロジェクト作成（backend フォルダ）
- [x] `/signup` `/login` API の仮実装（データ受け取りのみ）

### 🚧 進行中
- [ ] FastAPI と DB（SQLite）接続
- [ ] ユーザーテーブル作成
- [ ] `/signup` で DB にユーザー保存
- [ ] `/login` でパスワードチェック & JWT 発行

### 📅 今後の予定
- [ ] JWT を React 側で保持（localStorage）
- [ ] ログイン状態の管理（Context or Zustand）
- [ ] サークル登録 API 作成
- [ ] サークル参加 API 作成
- [ ] サークル一覧 / 詳細 API 作成
- [ ] UI のデザイン調整
