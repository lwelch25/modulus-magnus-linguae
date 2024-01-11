import urllib.request
import gzip
#Gets all the bible files, and creates a list if lists where the first entry is the language and second entry is the entire text of the bible


listoflangs = ['acu', 'af', 'agr', 'ake', 'am', 'amu', 'ar', 'bg', 'bsn', 'cak', 'ceb', 'ch', 'chq', 'chr', 'cjp', 'cni', 'cop', 'crp', 'cs', 'da', 'de', 'dik', 'dje', 'djk', 'dop', 'ee', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fi', 'fr', 'gbi', 'gd', 'gu', 'gv', 'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'jak', 'jap', 'jiv', 'kab', 'kbh', 'kek', 'kn', 'ko', 'la', 'lt', 'lv', 'mam', 'mi', 'ml', 'mr', 'my', 'ne', 'nhg', 'nl', 'no', 'ojb', 'pck', 'pes', 'pl', 'plt', 'pot', 'ppk', 'pt', 'quc', 'quw', 'ro', 'rom', 'ru', 'shi', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'ss', 'sv', 'syr', 'te', 'th', 'tl', 'tmh', 'tr', 'uk', 'usp', 'vi', 'wal', 'wo', 'xh', 'zh', 'zu']

txtfrombibles = []
for lang in listoflangs: 
    address = 'https://opus.nlpl.eu/download.php?f=bible-uedin/v1/mono/' + lang + '.text.gz'
    fish = urllib.request.urlopen(address)
    with gzip.open(fish, "rb") as f:
        cat = f.read()
    txtfrombibles.append([lang,cat])
