import requests
import json

product_ids = [
    [
        "1342",
        "womens-pu-slide-sandals"
    ],
    [
        "1050",
        "womens-capri-leggings-aop"
    ],
    [
        "1286",
        "girls-swimsuit-crop-top-aop"
    ],
    [
        "1285",
        "girls-hipster-swimsuit-bottom-aop"
    ],
    [
        "1185",
        "kids-leggings-aop"
    ],
    [
        "1097",
        "youth-leggings-aop"
    ],
    [
        "1110",
        "womens-shorts-aop"
    ],
    [
        "350",
        "womens-one-piece-swimsuit-aop"
    ],
    [
        "1241",
        "youth-full-length-leggings-aop"
    ],
    [
        "1218",
        "childrens-hoodie-aop"
    ],
    [
        "1209",
        "unisex-basketball-jersey-aop"
    ],
    [
        "859",
        "womens-full-zip-hoodie-aop"
    ],
    [
        "783",
        "womens-hoodie-dress-aop"
    ],
    [
        "1281",
        "loop-tie-side-bikini-bottom-aop"
    ],
    [
        "1274",
        "fully-lined-padded-sports-bra-aop"
    ],
    [
        "1223",
        "yoga-capri-leggings-aop"
    ],
    [
        "1023",
        "lightweight-sweatshirt-aop"
    ],
    [
        "977",
        "mens-elastic-beach-shorts-aop"
    ],
    [
        "365",
        "crew-socks"
    ],
    [
        "1290",
        "womens-workout-shorts-aop"
    ],
    [
        "1263",
        "womens-long-sleeve-dance-dress-aop"
    ],
    [
        "1260",
        "kids-pajama-pants-aop"
    ],
    [
        "361",
        "womens-vintage-swimsuit-aop"
    ],
    [
        "1255",
        "womens-long-sleeve-v-neck-shirt-aop"
    ],
    [
        "1217",
        "youth-joggers-aop"
    ],
    [
        "1174",
        "plus-size-leggings-aop"
    ],
    [
        "871",
        "mid-length-socks"
    ],
    [
        "702",
        "womens-bike-shorts-aop"
    ],
    [
        "701",
        "womens-capri-leggings-aop"
    ],
    [
        "1343",
        "mens-pu-slide-sandals"
    ],
    [
        "1280",
        "strappy-bikini-set-aop"
    ],
    [
        "960",
        "girls-sleeveless-sundress-aop"
    ],
    [
        "757",
        "mens-jogger-shorts-aop"
    ],
    [
        "740",
        "mens-pajama-pants-aop"
    ],
    [
        "700",
        "sports-bra-aop"
    ],
    [
        "360",
        "womens-classic-one-piece-swimsuit-aop"
    ],
    [
        "1078",
        "basketball-rib-shorts-aop"
    ],
    [
        "1062",
        "unisex-tank-top-aop"
    ],
    [
        "925",
        "womens-relaxed-shorts-aop"
    ],
    [
        "858",
        "apron-aop"
    ],
    [
        "1283",
        "mens-sports-shorts-aop"
    ],
    [
        "1087",
        "unisex-football-jersey-aop"
    ],
    [
        "947",
        "womens-casual-leggings-aop"
    ],
    [
        "822",
        "womens-baseball-jersey-aop"
    ],
    [
        "1289",
        "womens-short-sleeve-shirt-aop"
    ],
    [
        "1282",
        "strappy-triangle-bikini-top-aop"
    ],
    [
        "1222",
        "high-waisted-yoga-shorts-aop"
    ],
    [
        "1177",
        "womens-casual-shorts-aop"
    ],
    [
        "1132",
        "womens-biker-shorts-aop"
    ],
    [
        "1084",
        "athletic-long-shorts-aop"
    ],
    [
        "1037",
        "womens-satin-pajamas-aop"
    ],
    [
        "576",
        "baby-beanie-aop"
    ],
    [
        "508",
        "womens-mini-skirt-aop"
    ],
    [
        "1284",
        "girls-two-piece-swimsuit-aop"
    ],
    [
        "452",
        "recycled-poly-socks"
    ],
    [
        "934",
        "mens-puffer-jacket-aop"
    ],
    [
        "739",
        "womens-pajama-pants-aop"
    ],
    [
        "407",
        "womens-briefs-aop"
    ],
    [
        "919",
        "apron-aop"
    ],
    [
        "828",
        "womens-short-pajama-set-aop"
    ],
    [
        "1032",
        "mens-loose-t-shirt-aop"
    ],
    [
        "856",
        "mens-board-shorts-aop"
    ],
    [
        "1071",
        "seamless-sports-bra-aop"
    ],
    [
        "1028",
        "mens-hoodie-aop"
    ],
    [
        "799",
        "womens-bomber-jacket-aop"
    ],
    [
        "509",
        "womens-spandex-leggings-aop"
    ],
    [
        "949",
        "basketball-jersey-aop"
    ],
    [
        "948",
        "basketball-shorts-aop"
    ],
    [
        "1262",
        "womens-skater-dress-aop"
    ],
    [
        "703",
        "stretchy-leggings-aop"
    ],
    [
        "593",
        "mens-baseball-jersey-aop"
    ],
    [
        "1270",
        "athletic-hoodie-aop"
    ],
    [
        "1254",
        "mens-pajama-pants-aop"
    ],
    [
        "1251",
        "womens-pajama-pants-aop"
    ],
    [
        "997",
        "mens-tank-aop"
    ],
    [
        "832",
        "mens-full-zip-hoodie-aop"
    ],
    [
        "285",
        "womens-pencil-skirt-aop"
    ],
    [
        "923",
        "long-sleeve-kimono-robe-aop"
    ],
    [
        "281",
        "unisex-cut-and-sew-tee-aop"
    ],
    [
        "376",
        "sublimation-socks"
    ],
    [
        "924",
        "mens-hawaiian-shirt-aop"
    ],
    [
        "433",
        "mens-bomber-jacket-aop"
    ],
    [
        "589",
        "swim-trunks-aop"
    ],
    [
        "574",
        "cushioned-crew-socks"
    ],
    [
        "1242",
        "mens-polyester-tee-aop"
    ],
    [
        "591",
        "athletic-joggers-aop"
    ],
    [
        "831",
        "mens-baseball-jersey-aop"
    ],
    [
        "349",
        "womens-bikini-swimsuit-aop"
    ],
    [
        "256",
        "womens-cut-and-sew-casual-leggings-aop"
    ],
    [
        "279",
        "womens-cut-and-sew-tee-aop"
    ],
    [
        "450",
        "unisex-pullover-hoodie-aop"
    ],
    [
        "449",
        "unisex-sweatshirt-aop"
    ],
    [
        "978",
        "mens-mid-length-swim-shorts-aop"
    ],
    [
        "516",
        "high-waisted-yoga-leggings-aop"
    ],
    [
        "286",
        "womens-skater-skirt-aop"
    ],
    [
        "592",
        "fashion-hoodie-aop"
    ],
    [
        "406",
        "mens-boxer-briefs-aop"
    ],
    [
        "627",
        "crop-tee-aop"
    ],
    [
        "431",
        "t-shirt-dress-aop"
    ],
    [
        "276",
        "womens-cut-and-sew-racerback-dress-aop"
    ],
    [
        "1261",
        "mens-long-sleeve-shirt-aop"
    ],
    [
        "451",
        "unisex-zip-hoodie-aop"
    ]
]

objection = []
for bid in product_ids:

    url = "https://api.printify.com/v1/catalog/blueprints/" + bid[0] + "/print_providers.json"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImU5NmQyOGMyMmViYjYxNmI5MzljYzQxYTUyZDlmZGY5MjNlNTEzMmY0NTFmNjgzZGIwOGI2ZDAzZDAxMTFjMjRiNDcwODU1MDU0MjZlNDg2IiwiaWF0IjoxNjkwOTUzNDgzLjkzMjM0MywibmJmIjoxNjkwOTUzNDgzLjkzMjM0NywiZXhwIjoxNzIyNTc1ODgzLjkyNTc2Nywic3ViIjoiMTQwODIwNzciLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.AVeJKC7hKdnBS6qfsd8TBkR8-YYQ-xq-6x5rU37cXDruY8rRdJjpeQNC9WVbdBXxrRElmAxKCXiB7CwXPzw'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the response content to JSON
        objection.append({
            "id": bid[0],
            "name":bid[1],
            "provider": response.json()
        })
    else:
        print("Failed to fetch data from the API")
        print(response.text)

with open("output.json", "w") as json_file:
    json.dump(objection, json_file, indent=4)  # Write JSON data to the file with indentation
