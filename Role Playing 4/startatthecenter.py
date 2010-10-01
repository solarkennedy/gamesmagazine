#!/usr/bin/env python
# Role Playing 4 Solver
# Kyle Anderson 2010
# Under the AGPL 3

import MySQLdb
import copy
import os


#Did you import the imdb into your mysql using imdbpy ?
dbhost = 'localhost'
dbuser = 'imdb'
dbpass = 'imdb'
dbname = 'imdb'
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass,db=dbname)
cursor = db.cursor(MySQLdb.cursors.DictCursor)

blacklist = []
#blacklist = [4280,4108,84710,47297,4352,4392,4259,4400,4169,2074,67695,5654,4227,4102,3523,4423,6231,5720,4577,4394,2324,5612,35790,4409,6269,4223,4311,4263,4274,24840,3483,3496,22753,5005,24842,3497,57344,6076,4116,84843,67708,3435,2414,57343,20675,4578,24845,2614,45617,4396,4123,5751,84925,22747,3577,7242,4198,2215,24838,4287,4162,67702,2504,35679,5004,1954,67707,4203,4519,5025,2611,4149,5753,4432,24834,4302,93571,4308,5575,4439,4411,2507,5655,5802,4377,4353,7389,4375,4195,6143,4623,37891,4216,84837,84838,5734,4113,4283,84847,4911,3492,3522,4138,81144,3489,24839,67694,6124,4350,24844,67697,4269,7451,4398,6976,2071,84834,67699,4938,6712,6713,4279,3420,3486,3532,22744,67705,29811,84924,24831,93573,3462,4141,4348,2212,4171,4231,3477,6972,93575,4246,5703,2612,7163,4106,4913,2556,78500,5808,4100,1956,3533,34466,4281,5070,7169,4626,3582,2321,84960,7241,56555,3426,22746,7726,5805,3458,93606,4284,24837,64889,62639,6977,4256,35662,85068,4363,6602,24841,5803,4239,4177,6228,5573,29810,7450,4068,3407,4415,4337,6126,4914,5003,84841,4338,2854,83860,84851,6711,2326,35678,36163,1955,67696,70394,84846,22752,4506,6975,84836,5752,5609,5072,6056,36164,4277,6262,4915,4356,6078,6604,5588,4329,64891,4307,4575,3415,3376,4206,3515,5733,4255,4157,4624,4190,2853,71905,5629,3392,84842,4184,1953,4167,6710,4265,4268,2322,3516,4347,4247,4936,2555,5706,4261,2850,4395,4574,7728,3534,2412,6709,6635,4970,4625,5652,84849,4285,4224,4139,4313,6212,57345,5066,5026,4066,4267,4176,4063,4235,93574,3442,4822,4658,3511,4137,84848,4315,4215,4969,7239,2851,6102,2325,6621,53110,84839,3468,35857,4314,6213,6215,34463,4295,71773,31404,4185,6715,4291,29809,67468,67698,4820,4438,6636,5080,84844,93560,64947,4410,4270,4441,4148,6077,31402,4391,3580,5544,4264,3446,3460,3463,4399,64972,4214,2214,2216,4419,6671,7727,4272,5704,7180,24833,4656,4199,4320,4166,6103,71893,24836,4158,84942,4245,5806,84845,4657,5721,4823,3576,2415,2416,67700,22751,2503,4236,84850,6974,29812,58538,7240,4655,4334,5067,5810,5574,2557,2070,67730,4382,4355,4253,67706,4912,24835,7142,6264,4208,5065,6105,4373,2506,7452,29808,4576,4349,5804,3456,84840,1958,4393,3505,4507,5547,93572,5653,71904,2613,5735,84835,4234,4585,36162,64890,2213,4220,24843,84852,31403,6664,6267,4058,4328,4819,6625,35681,24832,4301,20674,2610,7390,4401,4225,5705,5006,2852,4209,4332,4821,4387,3579,5546,22745,4076,4075,3583,4351,35677,4252,4825,2413,4968,22754,4919,4222,15355,2072,4140,7204,4424,4362,6265,4318,35680,4180,5707,7453,196632,127273,101629,152919,165260,190837,110516,165267,153109,110514,117846,183031,110540,127274,127280,183036,190836,177708,166901,177607,165240,110491,183032,165280,160772,183110,144992,127277,109223,164083,165265,165262,183033,136017,165259,183112,165257,183035,153110,195008,165266,127278,110492,109222,194423,165256,183113,110513,177723,165263,109221,180530,165258,165264,166178,134025,109704,127276,177605,183034,109225,177724,127275,165273,110511,177606,190831,183037,110541,183030,183111,110512,190835,109224,127267,153113,153112,194607,127279,117845,165261,123538,133203,110515,153111,183029,267580,257544,202729,200107,279587,232109,283699,219862,249644,279589,271763,202727,267730,257575,202660,257574,202730,257543,257572,202661,279591,257545,270199,275701,284764,237935,247263,217486,202728,219923,273359,217461,279585,279586,268561,255345,208249,257573,279584,381991,340485,381869,381987,391826,381841,381986,340471,382002,340458,340474,391823,381970,340463,363720,381997,375055,391824,396806,381861,382007,340469,391805,396808,375053,381901,395805,382036,381995,375054,381873,340479,340349,382013,340476,381859,381992,396814,391804,351652,396800,381902,381982,386732,395806,381900,381835,381951,382000,396811,340477,381877,340468,382014,386731,382006,381905,322566,340473,381903,340481,381845,351651,351650,382010,381876,382039,381989,381875,340460,391827,382005,391825,383884,381999,381979,391829,396802,395538,382037,395895,391831,395754,340478,340464,381983,382011,375052,340472,340465,381860,381863,381990,381996,382008,395896,382012,382038,388642,340482,395626,340467,381984,396807,340459,391833,382001,381969,354909,337598,381906,340450,382004,381981,340470,391832,322988,340483,375056,381993,387195,340480,381865,396810,396186,337597,381904,396805,396812,340484,391830,381985,381994,381870,340447,340475,381952,381866,395947,375057,396804,381998,396801,381842,381980,381867,351609,381988,340461,391828,382003,381844,381864,382015,340462,381899,381871,381862,396809,381872,396813,396803,381843,381874,340466,381868,382016,382009,395539,401782,412504,403747,483960,483961,495348,496018,475826,483962,480700,484242,485204,445363,483488,489823,466651,477967,403748,484191,444465,460157,483963,445364,480701,477966,445362,401781,403749,481094,496020,454865,484066,496017,407596,484239,452341,484065,496019,540035,539636,539616,540165,540121,539840,540140,539938,539838,540334,540050,540172,547932,540005,597725,539933,540324,547926,547921,539751,547937,547923,539888,540131,540194,540145,521917,540290,540267,540049,540150,540161,564926,547911,539651,539851,539750,540025,539662,539903,540134,539622,539772,540133,540151,540427,559461,541750,539940,539808,539864,540072,539871,557746,540038,535652,582930,540156,539824,539853,539865,539882,540154,540437,539883,540278,540032,540063,539686,540125,540143,540263,540391,547925,540268,539912,539615,539955,540031,539936,539856,540079,540084,539786,539693,539765,540291,540317,540029,547920,539737,539650,539844,541751,540351,539900,540260,510763,539752,541749,539746,582932,539965,575491,539925,594826,540276,540372,572419,539699,540375,594844,547913,540431,539640,512927,539789,540257,539944,582931,539813,580894,541348,540067,539956,539977,539881,540098,539633,540307,539825,547912,539687,539821,580903,555663,540123,539826,539983,540046,539704,539970,547942,540226,540021,540358,539738,540080,539702,540398,539886,540252,540155,540010,539866,557140,540371,540014,545043,539962,540091,539785,540006,540087,539654,540316,597721,540022,539762,540170,510505,539763,580146,539823,540239,551094,539756,572418,539961,540159,539718,580906,540083,539917,539810,540283,540428,512932,580904,540249,539895,539855,539891,540245,539805,539804,540430,580902,539753,543438,539926,540288,546159,540319,582935,542307,540369,539870,540167,540318,553874,527418,547919,540181,540389,540030,540521,540196,580895,539812,540024,570163,540303,539960,539976,540240,557747,539974,540089,539787,539834,547924,539613,539902,539791,549058,540376,560036,539730,563960,539935,557842,540259,540308,540012,539817,547944,539924,539836,540193,597719,540195,539759,539727,540044,540043,512928,597715,539691,539878,540309,539885,540034,597716,539728,539951,539816,540282,582925,540230,510506,540253,540187,540363,539716,539904,512929,563170,540280,540402,540164,540401,540248,539637,539967,539845,539849,540304,540393,540188,542082,539701,539666,543440,540042,539724,539937,547940,540233,539969,540208,539725,582936,512934,540365,539790,539778,540231,539934,539950,593949,568525,540097,540362,582934,540305,547927,539620,540235,539966,539918,540286,540191,540190,540015,539664,580162,540315,540356,540255,539653,539614,539868,540057,539943,591716,540178,539692,539899,539618,540399,547938,539978,540361,521915,588198,539735,597717,539754,540244,547945,539914,540023,539766,540330,597718,539712,501839,547934,539894,540272,580901,540332,539698,540068,547910,539835,539887,540292,539771,540146,594827,540056,539901,540229,539736,539928,547935,540320,539638,540397,540152,539663,561224,539916,547947,540026,539959,539964,539717,580167,597724,539734,539818,539689,540246,539758,539975,540052,539952,540262,539927,540153,540429,539748,540284,540277,540238,540326,540279,582926,540069,539892,540274,540339,540169,539788,540396,540265,539942,540522,512930,540328,540177,540323,539847,540264,539619,547918,547936,566806,513799,540092,540065,539760,539982,539884,539893,539828,539722,539860,540040,541752,557922,539939,539833,540310,540004,540338,540285,582928,539774,547943,539809,540232,540157,540301,580908,540321,540180,543129,539768,540013,540017,539776,540048,539915,540314,540142,543442,540302,539773,540313,540390,540028,539700,540266,539705,539779,540287,540008,540086,539668,540039,540325,539723,540139,535116,540312,539945,568175,539896,539848,539852,539829,540054,540241,539815,540036,582927,540128,540373,540189,540368,540327,540289,543441,540360,540174,540271,540041,540394,598309,547946,539839,540122,557921,540234,540395,539800,540425,540053,579503,539854,540047,539733,540045,539767,540058,582933,578628,540250,540073,540225,539807,539690,539947,539913,539802,540258,539832,539621,545054,539831,539706,541347,509925,547939,540136,568480,539667,540166,540027,540011,539968,539665,540163,591714,539634,540354,539713,540007,539958,539801,540370,540335,540269,547922,540085,557844,539726,540275,539793,540059,539954,540033,512926,547941,597762,539775,563961,540130,539963,545037,594828,580893,539770,540018,540019,540126,540137,539617,540243,540523,540173,540182,582339,540336,540333,543439,539652,540197,540340,557754,539715,540037,540160,540081,539703,539635,597720,539688,539721,510766,551095,539953,540144,539777,540353,539822,540273,539720,539846,539867,540060,580907,540090,539729,512931,557843,580905,540149,521916,540337,540009,547914,540426,540175,566940,539946,582929,597723,540306,539869,540311,539719,539819,540016,597722,540135,540064,540228,540147,540158,642421,675946,670734,604054,639727,624887,612735,675951,675948,624925,671066,605744,642443,675945,690003,646273,612655,664242,602543,640664,675949,604053,612656,642411,607234,601506,624910,670733,602025,675944,612658,642447,687704,675955,665811,624888,682714,625080,643015,673269,612660,675952,602542,607237,642410,642450,642448,675954,616024,698999,601507,642784,621842,646272,675942,670735,612659,602544,642449,628494,646274,602014,625017,675953,642406,600267,639726,605119,675950,663341,621019,624919,675943,624882,687870,675947,624883,603378,604821,665556,671067,612657,799473,799477,777879,799450,767632,737000,718748,721877,759525,720957,722018,759235,721558,701775,799486,799463,787916,799468,799461,799472,799455,799484,736980,826171,826174,820775,826170,821009,824057,826172,899798,826168,826933,830847,917261,955204,956647,987565,913645,986735,962591,986557,913633,911738,944961,903157,943605,1088579,1068901,1068917,1053978,1052162,1054464,1076141,1054149,1009474,1033879,1054102,1005539,1053819,1084705,1052871,1088580,1053777,1012559,1062919,1071353,1071337,1007584,1067929,1041035,1084704,1067966,1068903,1190340,1192221,1173959,1171879,1171880,1173960,1171881,1189745,1137496,1173958,1171882,1280680,1249730,1214495,1215494,1214498,1242598,1202666,1231975,1255568,1249731,1241643,1262891,1214492,1214496,1293237,1210122,1214497,1262965,1214494,1214493,1263074,1214499,1244285,1263028,1213592,1263233,1261148,1214500,1366843,1360951,1368280,1323256,1364138,1397382,1310329,1366844,1364546,1366848,1364137,1377840,1307524,1310330,1434168,1489897,1472820,1419069,1417240,1484038,1447929,1492036,1462385,1419039,1456079,1462384,1475902,1434167,1419265,1554791,1555930,1554792,1510303,1504965,1553779,1510305,1565481,1519013,1543572,1504474,1510304,1519004,1505632,1533641,1554797,1591540,1544578,1519014,1553762,1554803,1602121,1667373,1633643,1633664,1652061,1621947,1621948,1602119,1602122]

class actorclass:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = ()
   movies = []
   links = ()
   regex = ""
   name = ""
   coworkers = []
class movieclass:
   """ Class for storing movie info """
   possibilities = []
   name = ""

movie = []
for x in range(13):
   movie.append(movieclass())
   movie[x].name = x

actor = []
for x in range(9):
   actor.append(actorclass())


#The example diagram they give is first, last but the imdb data is last,first
#Question marks stand for 3,4,6, or 9
# Gener in the imdb, 1 is male and 2 is female
actor[0].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{5} '
actor[0].links = ( movie[12], movie[1] )
actor[0].gender= 2
actor[1].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{5} '
actor[1].links = ( movie[0], movie[1] )
actor[1].gender= 1
actor[2].regex = '^[^- ,]{8}, (([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})) '
actor[2].links = ( movie[1], movie[2] )
actor[2].gender= 1
actor[3].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{7} '
actor[3].links = ( movie[3], movie[4] )
actor[3].gender= 2
actor[4].regex = '^[^- ,]{7}, (([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})) '
actor[4].links = ( movie[5], movie[6], movie[7] )
actor[4].gender= 2
actor[5].regex = '^[^- ,]{7}, [^- ,]{7} '
actor[5].links = ( movie[7], movie[8] )
actor[5].gender= 2
actor[6].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{7} '
actor[6].links = ( movie[9], movie[10] )
actor[6].gender= 1
actor[7].regex = '^[^- ,]{7}, (([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})) '
actor[7].links = ( movie[11], movie[12] )
actor[7].gender= 2
actor[8].links = ( movie[0],  movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], movie[8], movie[9], movie[10], movie[11], movie[12] )
actor[8].gender = 2

# For speed, we have the actor lists prepopulated in this file
execfile("actorpossibilities.py")

def actorname(id):
        cursor.execute("SELECT `name` FROM `name` WHERE `id` = '%s'" % (id))
        Results = cursor.fetchall()
	return Results[0]['name']
def moviename(id):
        cursor.execute("SELECT `title` FROM `title` WHERE `id` = '%s'" % (id))
        Results = cursor.fetchall()
        return Results[0]['title']
def gender(id):
	cursor.execute("SELECT `role_id` FROM `cast_info`,`title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (id) )
        Results = cursor.fetchall()
        return Results[0]['role_id']

def isthereanactressinthislist(thelist):
	for a in thelist:
		if gender(a) == 2:
			return True
	return False
def moviesincommon(actor1, actor2):
	cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (actor1) )
        SqlResults = cursor.fetchall()
        movielist1 = list(set([mov['movie_id'] for mov in SqlResults]))
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (actor2) )
        SqlResults = cursor.fetchall()
        movielist2 = list(set([mov['movie_id'] for mov in SqlResults]))
	commonmovies = list(set(movielist1).intersection(set(movielist2)) )
	return [i for i in commonmovies if i not in blacklist ]
def humanmoviesincommon(actor1, actor2):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (actor1) )
        SqlResults = cursor.fetchall()
        movielist1 = list(set([mov['movie_id'] for mov in SqlResults]))
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (actor2) )
        SqlResults = cursor.fetchall()
        movielist2 = list(set([mov['movie_id'] for mov in SqlResults]))
        commonmovies = tuple( set(movielist1).intersection(set(movielist2)) )
	print [moviename(i) for i in commonmovies]
	



def moviestheyhavebeenin(actor):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (actor) )
        SqlResults = cursor.fetchall()
        # We have a tuple of dictionaries from our mysql, but we just want a big tuple:
        return list(set([mov['movie_id'] for mov in SqlResults]))

def prettyprint(thelist):
	print [actorname(i) for i in thelist]

def recurse(level, centeractress, placedactors):
#def recurse(level, centeractress, placedactors, placedmovies):
	if level == 4:
		print "We have reached the end:"
		prettyprint(placedactors)
		print placedactors
		return

	for possibleactor in actor[level].possibilities:
		if possibleactor not in placedactors:
			sharedmovies = moviesincommon(centeractress, possibleactor)
			if len(sharedmovies) >= len(actor[level].links):
				recurse(level+1, centeractress, copy.copy(placedactors + [possibleactor]))
	
print "Going through " + str(len( actor[8].possibilities)) + " actresses for the center"
for actress in actor[8].possibilities:
	#Go through each actress and try to fit it into the puzzle
	placedactors = []
	placedmovies = []
	print "We are recursing with " + actorname(actress) + " (" + str(actress) + ")"
	recurse(0, actress, copy.copy(placedactors) )
	#recurse(0, centeractress, copy.copy(placedactors), copy.copy(placedmovies) )

