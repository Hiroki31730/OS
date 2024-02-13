import glob
import os
def row_word(r): # 単語数と行数カウントする
    row_count = 0 # 行数
    word_count = 0 # 単語数
    with open(r) as f_rw:
        for l in f_rw:
            if l.endswith('\n'):
                row_count = row_count + 1
            word_count = word_count + len(l.split())
    return row_count, word_count

path = "/Users/e205726/college" 
all_file = [] # 取得したファイルのパスのリスト
count = 0
ps = glob.glob(path + '/*')
while count == 0 or judge == 1: # ディレクトリ内のファイルのパスを全てリストに格納する
    judge = 0
    all_dir = [] # さらにglob.glob()で読み込む必要のあるディレクトリのリスト
    for p in ps: # ディレクトリ内のファイルとディレクトリを仕分けする
        if os.path.isdir(p):
            for p2 in glob.glob(p + '/*'):
                all_dir.append(p2)        
        else:
            all_file.append(p)
    if not all_dir: # さらに読み込む必要のあるディレクトリが存在するかの確認
        pass
    else:
        judge = 1 # ループする
    count = count + 1
    ps = all_dir # 次に読み込むディレクトリのリスト更新

row_al = 0 # 総行数
word_al = 0 # 総単語数
size_al = 0 # 総ファイルサイズ

for f in all_file:
    if f.endswith(('.py','.java','.c','.go')):
        row, word = row_word(f)
        list = [str(row), str(word), str(os.path.getsize(f)), f]
        print(" ".join(list))
        row_al = row_al + row
        word_al = word_al + word
        size_al = size_al + os.path.getsize(f)
list_al = [str(row_al), str(word_al), str(size_al), 'total']
print(" ".join(list_al))
