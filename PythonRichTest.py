from rich.console import Console
from rich.table import Table
from rich.progress import track
import requests
import json

#
#郵便番号検索APIを利用して、郵便番号から住所を取得する
#

#定数定義
RESULTS = "results"

CLM_ADDRESS1 = "address1"
CLM_ADDRESS2 = "address2"
CLM_ADDRESS3 = "address3"
CLM_KANA1 = "kana1"
CLM_KANA2 = "kana2"
CLM_KANA3 = "kana3"
CLM_CODE = "code"
CLM_ZIPCODE = "zipcode"

#----------------------
#メイン処理
#----------------------
def main():
    console = Console()
    zipcode = input_zipcode()
    r = get_address(zipcode)

    if r:
        table = create_result_table(r)
        console.print(table)

#----------------------
#郵便番号入力受付
#----------------------
def input_zipcode():

    while(True):

        #ユーザ入力受付
        print("郵便番号を数字7桁で入力してください")
        zipcode = input()
    
        #数値チェック
        is_int = zipcode.isdigit()

        #桁数チェック
        zip_len = len(zipcode)
        
        if is_int and zip_len == 7:
            break

    return zipcode

#----------------------
#郵便番号から住所取得
#----------------------
def get_address(zipcode):
    try:
        r = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + zipcode)

        if r.status_code == 200:
            print("Request successful")
        else:
            print("Request failed")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        r = None
    return r

#----------------------
#結果テーブル作成
#----------------------
def create_result_table(r):
    json_dict = json.loads(r.text)

    table = Table(show_header=True, header_style="bold magenta", title="Results")

    #ヘッダ部作成
    for key in json_dict[RESULTS][0]:
        table.add_column(key, style="dim", width=20)

    #データ部作成
    val_list = list(json_dict[RESULTS][0].values())
    
    table.add_row(*val_list)

    return table

#----------------------
#呼び出し判定
#----------------------
if __name__ == "__main__":
    # このコードはファイルが直接実行された場合にのみ実行されます
    print("This file was run directly")
    main()
    input() #待ち状態にする

else:
    # このコードはファイルがモジュールとしてインポートされた場合にのみ実行されます
    print("This file was imported as a module")
