from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RealmRaidAssets: 


	# Image Rule Assets
	# 点击结界突破的图片 
	I_REALM_RAID = RuleImage(roi_front=(246,628,63,64), roi_back=(246,628,63,64), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_realm_raid.png")
	# 五个勋章 
	I_MEDAL_5 = RuleImage(roi_front=(238,205,212,53), roi_back=(216,187,919,364), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_5.png")
	# description 
	I_MEDAL_4 = RuleImage(roi_front=(241,483,193,46), roi_back=(228,178,899,362), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_4.png")
	# description 
	I_MEDAL_3 = RuleImage(roi_front=(240,210,193,41), roi_back=(229,189,894,345), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_3.png")
	# description 
	I_MEDAL_2 = RuleImage(roi_front=(572,478,198,48), roi_back=(217,193,923,354), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_2.png")
	# description 
	I_MEDAL_1 = RuleImage(roi_front=(570,206,199,52), roi_back=(237,198,892,336), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_1.png")
	# 没有勋章的 
	I_MEDAL_0 = RuleImage(roi_front=(510,336,202,51), roi_back=(231,200,898,336), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_0.png")
	# 右上角红色的关闭 
	I_BACK_RED = RuleImage(roi_front=(1178,101,57,64), roi_back=(1178,101,57,64), threshold=0.7, method="Template matching", file="./tasks/RealmRaid/res/res_back_red.png")
	# 没有锁的状态图标 
	I_UNLOCK = RuleImage(roi_front=(818,579,38,42), roi_back=(818,579,38,42), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_unlock.png")
	# 以锁的状态图片 
	I_LOCK = RuleImage(roi_front=(818,579,36,41), roi_back=(818,579,36,41), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_lock.png")
	# 刷新按钮 
	I_FRESH = RuleImage(roi_front=(957,564,182,66), roi_back=(957,564,182,66), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_fresh.png")
	# 点击的式神录 
	I_SHIKIGAMI = RuleImage(roi_front=(1206,608,54,51), roi_back=(1206,608,54,51), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_shikigami.png")
	# 进攻 
	I_FIRE = RuleImage(roi_front=(982,494,136,63), roi_back=(140,129,1024,584), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_fire.png")
	# 打完个后出现的领取奖励 
	I_SOUL_RAID = RuleImage(roi_front=(577,502,100,100), roi_back=(577,502,100,100), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_soul_raid.png")
	# 刷新确认 
	I_FRESH_ENSURE = RuleImage(roi_front=(672,403,173,59), roi_back=(672,403,173,59), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_fresh_ensure.png")
	# 没有锁图片，适配呱太入侵 
	I_UNLOCK_2 = RuleImage(roi_front=(1002,643,30,41), roi_back=(1002,643,30,41), threshold=0.9, method="Template matching", file="./tasks/RealmRaid/res/res_unlock_2.png")
	# 以锁图片，适配呱太 
	I_LOCK_2 = RuleImage(roi_front=(1002,645,34,38), roi_back=(1002,645,34,38), threshold=0.9, method="Template matching", file="./tasks/RealmRaid/res/res_lock_2.png")
	# description 
	I_MEDAL_5_FROG = RuleImage(roi_front=(903,479,201,49), roi_back=(189,182,967,376), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_5_frog.png")
	# 3徽章新图2号 
	I_MEDAL_3_2 = RuleImage(roi_front=(575,489,188,32), roi_back=(575,489,188,32), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_3_2.png")
	# description 
	I_MEDAL_3_3 = RuleImage(roi_front=(902,479,201,50), roi_back=(902,479,201,50), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_medal_3_3.png")


	# Image Rule Assets
	# 出现呱太勋章 
	I_FROG_MEDAL = RuleImage(roi_front=(912,12,32,35), roi_back=(912,12,32,35), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_frog_medal.png")
	# 已经进攻三次了 
	I_RR_THREE = RuleImage(roi_front=(346,584,42,44), roi_back=(346,584,42,44), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_rr_three.png")
	# 呱太入侵， 第一次进入结界时候出现 
	I_FROG_RAID = RuleImage(roi_front=(511,301,282,100), roi_back=(511,301,282,100), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_frog_raid.png")
	# 个人 
	I_RR_PERSON = RuleImage(roi_front=(1203,236,56,100), roi_back=(1203,236,56,100), threshold=0.8, method="Template matching", file="./tasks/RealmRaid/res/res_rr_person.png")


	# Ocr Rule Assets
	# 刷新的时间 
	O_FRESH_TIME = RuleOcr(roi=(1042,582,85,36), area=(0,0,100,100), mode="Duration", method="Default", keyword="", name="fresh_time")
	# 右上角 突破卷的数量 
	O_NUMBER = RuleOcr(roi=(1143,13,80,39), area=(0,0,100,100), mode="DigitCounter", method="Default", keyword="", name="number")
	# Ocr-description 
	O_FROG_1 = RuleOcr(roi=(158,168,42,33), area=(158,168,42,33), mode="Digit", method="Default", keyword="", name="frog_1")
	# Ocr-description 
	O_FROG_2 = RuleOcr(roi=(491,170,34,32), area=(491,170,34,32), mode="Digit", method="Default", keyword="", name="frog_2")
	# Ocr-description 
	O_FROG_3 = RuleOcr(roi=(824,170,34,32), area=(824,170,34,32), mode="Digit", method="Default", keyword="", name="frog_3")
	# Ocr-description 
	O_FROG_4 = RuleOcr(roi=(158,303,38,35), area=(158,303,38,35), mode="Digit", method="Default", keyword="", name="frog_4")
	# Ocr-description 
	O_FROG_5 = RuleOcr(roi=(489,304,35,35), area=(489,304,35,35), mode="Digit", method="Default", keyword="", name="frog_5")
	# Ocr-description 
	O_FROG_6 = RuleOcr(roi=(824,305,35,33), area=(824,305,35,33), mode="Digit", method="Default", keyword="", name="frog_6")
	# Ocr-description 
	O_FROG_7 = RuleOcr(roi=(160,439,31,33), area=(160,439,31,33), mode="Digit", method="Default", keyword="", name="frog_7")
	# Ocr-description 
	O_FROG_8 = RuleOcr(roi=(494,441,31,31), area=(494,441,31,31), mode="Digit", method="Default", keyword="", name="frog_8")
	# Ocr-description 
	O_FROG_9 = RuleOcr(roi=(825,440,33,33), area=(825,440,33,33), mode="Digit", method="Default", keyword="", name="frog_9")


	# Click Rule Assets
	# 用来分割不同的挑战位置 
	C_PARTITION_1 = RuleClick(roi_front=(233,147,229,120), roi_back=(233,147,229,120), name="partition_1")
	# 用来分割不同的挑战位置 
	C_PARTITION_2 = RuleClick(roi_front=(566,148,237,115), roi_back=(566,148,237,115), name="partition_2")
	# 用来分割不同的挑战位置 
	C_PARTITION_3 = RuleClick(roi_front=(895,147,232,116), roi_back=(895,147,232,116), name="partition_3")
	# 用来分割不同的挑战位置 
	C_PARTITION_4 = RuleClick(roi_front=(236,283,229,124), roi_back=(236,283,229,124), name="partition_4")
	# 用来分割不同的挑战位置 
	C_PARTITION_5 = RuleClick(roi_front=(564,280,237,120), roi_back=(564,280,237,120), name="partition_5")
	# 用来分割不同的挑战位置 
	C_PARTITION_6 = RuleClick(roi_front=(899,282,232,120), roi_back=(899,282,232,120), name="partition_6")
	# 用来分割不同的挑战位置 
	C_PARTITION_7 = RuleClick(roi_front=(233,416,236,121), roi_back=(233,416,236,121), name="partition_7")
	# 用来分割不同的挑战位置 
	C_PARTITION_8 = RuleClick(roi_front=(567,413,230,124), roi_back=(567,413,230,124), name="partition_8")
	# 用来分割不同的挑战位置 
	C_PARTITION_9 = RuleClick(roi_front=(897,418,230,116), roi_back=(897,418,230,116), name="partition_9")


