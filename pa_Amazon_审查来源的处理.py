import requests
url = "https://www.amazon.cn/gp/product/B07F3KDKDW/ref=s9_acsd_hps_bw_c_x_1_w?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=JS8XNQAHK81M2WGTRRQ6&pf_rd_t=101&pf_rd_p=3f149c06-7221-4924-a124-ebbe0310b38c&pf_rd_i=116169071"
try:
	kv = {'user-agent':'Mozilla/5.0'}   #应对爬虫审查
	r = requests.get(url,headers=kv)
	r.raise_for_status()      			#若返回值不是202，则抛出一个异常
	r.encoding = r.apparent_encoding
except:
	print("进入爬取失败")
