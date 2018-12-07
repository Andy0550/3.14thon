# Michael Dvořák
# Python_3.7.0

import string


text = "zwmcp zwmcp, nepvwvm npwmrz,wv zrc hapcuzu ah zrc vwmrz;oriz wqqapzil rivx ap cyc,saelx hpiqc zry hciphel uyqqczpy?wv oriz xwuzivz xccfu ap ugwcu.nepvz zrc hwpc ah zrwvc cycu?av oriz owvmu xipc rc iufwpc?oriz zrc rivx, xipc ucwdc zrc hwpc?ivx oriz uraelxcp, ivx oriz ipz,saelx zowuz zrc uwvcou ah zry rcipz?ivx orcv zry rcipz ncmiv za nciz,oriz xpcix rivx? ivx oriz xpcix hccz?oriz zrc riqqcp? oriz zrc sriwv,wv oriz hepvisc oiu zry npiwv?oriz zrc ivjwl? oriz xpcix mpiuf,xipc wzu xcixly zcppapu sliuf!orcv zrc uzipu zrpco xaov zrcwp ufcipuivx oizcp’x rcijcv owzr zrcwp zcipu:xwx rc uqwlc rwu oapg za ucc?xwx rc ora qixc zrc liqn qigc zrcc?zwmcp zwmcp nepvwvm npwmrz,wv zrc hapcuzu ah zrc vwmrz:oriz wqqapzil rivx ap cyc,xipc hpiqc zry hciphel uyqqczpy?"
text2 = "Life is like a box a chocolate, you never know what your going to get."
text3 = "Lwhc wu lwgc i nat i srasalizc, yae vcjcp gvao oriz yaep mawvm za mcz."

def affine_cipher(text,en):
    letters = string.ascii_lowercase
    if en == True:
        for x in text:
            if x in letters:
                y = (5*letters.index(x)+8)
                print(letters[y%26],end="")
            else:
                print(x,end="")
    elif en == False:
        for x in text:
            if x in letters:
                y = 21*((letters.index(x)) - 8)
                print(letters[y%26], end="")
            else:
                print(x,end="")
    print()

#affine_cipher(text,False)
affine_cipher(text2,True)
affine_cipher(text3,False)
    
    
