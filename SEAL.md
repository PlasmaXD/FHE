

```bash
git clone https://github.com/microsoft/SEAL.git
cd SEAL
cmake -S . -B build
cmake --build build
```

こちらの説明に基づいて、Microsoft SEALのPythonバインディングをUbuntu環境でビルドして使用するための手順を整理します。このPythonバインディングは、Huelseが提供しているSEAL-Pythonというリポジトリを使用します。以下のステップは、GitHubリポジトリから直接クローンしてビルドするプロセスを説明しています。

### ステップ 1: 必要な依存関係のインストール

Ubuntuに必要なツールとライブラリをインストールします。この手順には、CMake、Python3、および開発ツールが含まれます。

```bash
sudo apt-get update
sudo apt-get install git build-essential cmake python3 python3-dev python3-pip
```

### ステップ 2: リポジトリのクローンと依存ライブラリのインストール

GitHubからSEAL-Pythonリポジトリをクローンし、必要なPythonライブラリをインストールします。

```bash
git clone https://github.com/Huelse/SEAL-Python.git
cd SEAL-Python
pip3 install numpy pybind11
```

### ステップ 3: サブモジュールの更新

SEALとpybind11のサブモジュールを初期化し、更新します。

```bash
git submodule update --init --recursive
```

### ステップ 4: Microsoft SEALライブラリのビルド

SEALライブラリをビルドするために、CMakeを使用します。圧縮ライブラリを無効にしてビルドを行います。

```bash
cd SEAL
cmake -S . -B build -DSEAL_USE_MSGSL=OFF -DSEAL_USE_ZLIB=OFF -DSEAL_USE_ZSTD=OFF
cmake --build build
cd ..
```

### ステップ 5: Pythonバインディングのビルド

Pythonバインディングをビルドするために `setup.py` を実行します。

```bash
python3 setup.py build_ext -i
```

### ステップ 6: ビルドしたバインディングのテスト

ビルドした動的ライブラリ（`.so` ファイル）をexamplesディレクトリにコピーし、サンプルコードを実行して動作を確認します。

```bash
cp seal.*.so examples
cd examples
python3 4_bgv_basics.py
```

これで、Microsoft SEALのPythonバインディングをUbuntuでビルドし、基本的な例を実行してライブラリの動作をテストすることができました。他の例も同様に実行してみるとより多くの機能について学ぶことができます。この手順により、PythonからSEALライブラリを利用するための準備が整います。