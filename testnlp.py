# coding:utf-8

import jieba, jieba.analyse, os

files = os.listdir('./news')
for f in files:
	news = open('./news/' + f).read()
	try:
		news = news.decode('utf-8')
	except UnicodeDecodeError:
		news = news.decode('gbk','ignore')
		
	word_list = jieba.cut(news)
	# print ' '.join(word_list)

	fs = open('./keyword/' + f, 'w')
	for x in jieba.analyse.extract_tags(news,topK=20,withWeight=True):
		print '%s\t%f' % x
		fs.write('%s\t%f\n' % (x[0].encode('utf-8'),x[1]))
		
	fs.close()