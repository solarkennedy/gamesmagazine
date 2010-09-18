<?php

init();
print_r($statearray);
while(insertstates() <= 21) {
init();
echo "next\n";
};

printarray();


function checkit($location) {
$direct=7;
if (validspot($location,$direct)) {
echo "1";
} else {
echo "0";
}
}

function array_remove_value() {
    $args = func_get_args();
    $arr = $args[0];
    $values = array_slice($args,1);

    foreach($arr as $k=>$v) {
        if(in_array($v, $values))
            unset($arr[$k]);
    }
    return $arr;
}

function array_remove_key ()
{
  $args  = func_get_args();
  return array_diff_key($args[0],array_flip(array_slice($args,1)));
}
function array_remove($arr,$value) {

   return array_values(array_diff($arr,array($value)));

}




function stateremove($state) {
global $statearray;

$statearray = array_remove_key($statearray,array_search($state,$statearray));
#echo " I want to remove $state from the statearray which is at element " . array_search($state,$statearray) ."\n";
}
function stateremove2($state) {
global $doublestates;

$doublestates = array_remove_key($doublestates,array_search($state,$doublestates));
#echo " I want to remove $state from the statearray which is at element " . array_search($state,$statearray) ."\n";
}

function insertstates() {
global $thearray;
global $statearray;
global $doublestates;
$statecounter=0;
$counter=1;
while (($counter != 0) && ($counter <= 113)) {
        foreach ($doublestates as $state) {
                #if ($thearray[$counter] == "0") {
                if (($thearray[$counter] == $state[0]) || ($thearray[$counter] == "0")) {
#               echo "Location $counter has a value of " . $thearray[$counter] . " and our state starts with " . $stateletters[0] . "\n";       
                        if (trystate($state, $counter, 4)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state, $counter, 7)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state,$counter, 8)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state, $counter, 5)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state, $counter, 6)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state, $counter, 1)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state, $counter, 3)) {
                        $statecounter++;
                        stateremove2($state);
                        } elseif (trystate($state, $counter, 2)) {
                        $statecounter++;
                        stateremove2($state);
                        }
                }#If therer is a 0
        }#end fhile
        $counter++;
} #end each state
$statecounter=$statecounter*2;

$counter=1;
while (($counter != 0) && ($counter <= 113)) {
	foreach ($statearray as $state) {
		#if ($thearray[$counter] == "0") {
		if (($thearray[$counter] == $state[0]) || ($thearray[$counter] == "0")) {
#		echo "Location $counter has a value of " . $thearray[$counter] . " and our state starts with " . $stateletters[0] . "\n";	
			if (trystate($state, $counter, 4)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state, $counter, 7)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state,$counter, 8)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state, $counter, 5)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state, $counter, 6)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state, $counter, 1)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state, $counter, 3)) {
			$statecounter++;
			stateremove($state);
			} elseif (trystate($state, $counter, 2)) {
			$statecounter++;
			stateremove($state);
			}
		}#If therer is a 0
	}#end fhile
	$counter++;
} #end each state
#$statecounter=$statecounter+4;
echo "I could fit $statecounter states!\n";
return $statecounter;
} #endfunction

function printarray() {
global $thearray;
global $statearray;
foreach ($thearray as $index => $value) {
    echo $value  . " " ;
	if (($index - 8) % 15 == 0 ) { 
	echo "\n "; 
	} elseif (($index) % 15 == 0 ) {
	echo "\n"; }
	}
}

function init() {
#header("Content-type: text/plain"); 
global $thearray;
global $thearray2;
$thearray = array_fill(1,113, '0');
$thearray2= range(1,113);
shuffle($thearray2);
$filename = "states";
global $statearray;
global $doublestates;
$statearray = file($filename,  FILE_IGNORE_NEW_LINES   );
shuffle($statearray);
#$doublestates=array("vermontana","floridaho","arkansas");
$doublestates=array("vermontana","westvirginia","floridaho","arkansas");
#shuffle($doublestates);
#$statearray=array_merge($doublestates,$statearray);

}

function trystate($state, $location, $direction) {
global $thearray;
#$stateletters = str_split($state);
#echo "Trying $state at location $location on direction $direction\n";
if (fitstate($state, $location, $direction)) {
echo "Placing $state at location $location in direction $direction\n";
placestate($state, $location, $direction);
return true; 
} else {
return false; 
}


}#end function


function fitstate($state, $location, $direction) {
global $thearray;
#$stateletters = str_split($state);
if (($thearray[$location] == $state[0]) || ($thearray[$location] == "0")) {
	#The letter we need is already here!
	if (strlen($state) == 1) {
		return true;
	} elseif (validspot($location, $direction)) {
		$newstate = substr($state, 1);
		return fitstate($newstate, nextspot($location, $direction), $direction);
	} else {
		#echo "Won't fit\n";
		return false;
	}
} else {
	return false;
	#The space was occupied
}#End letter check

} # end fitstate function


function placestate($state, $location, $direction) {
global $thearray;
#$stateletters = str_split($state);
if (strlen($state) == 0) {
		return true;
} else {
		$thearray[$location] = $state[0];
		$newstate = substr($state, 1);
		return placestate($newstate, nextspot($location, $direction), $direction);
}
}#end placestate function

function validspot($location, $direction) {
if ($direction == 1) {
	if (oddrow($location)) { 
		if (($location-8) %  15 <> 0) {
		return true;
		} else {
		return false;
		}
	} else {
		return false; #if we are on an even row going to the right, we are done
	}
} elseif ($direction == 2) {
	if (($location  <= 113) && ($location >= 106)) {
		return false;
	} elseif ((($location-8) %  15 <> 0) && (($location-15) %  15 <> 0)) {
		return true;
	} else {
		return false;
	}
} elseif ($direction == 3) {
	if (oddrow($location)) { 
		if (($location  <= 113) && ($location >= 106)) {
		return false;
		} else {
		return true;
		}
	} else {
		return false; #if we are on an even row going to the right, we are done
	}
} elseif ($direction == 4) {
	if (($location  <= 113) && ($location >= 106)) {
		return false;
	} elseif ((($location-1) %  15 <> 0) && (($location-9) %  15 <> 0)) {
		return true ;
	} else {
		return false;
	}
} elseif ($direction == 5) {
	if (oddrow($location)) { 
		if (($location-1) %  15 <> 0) {
		return true;
		} else {
		return false;
		}
	} else {
		return false; #if we are on an even row going to the right, we are done
	}
} elseif ($direction == 6) {
	if (($location  <= 8) && ($location >= 0)) {
		return false;
	} elseif ((($location-1) %  15 <> 0) && (($location-9) %  15 <> 0)) {
		return true;
	} else {
		return false;
	}
} elseif ($direction == 7) {
	if (oddrow($location)) { 
		if (($location  <= 8) && ($location >= 0)) {
		return false;
		} else {
		return true;
		}
	} else {
		return false; #if we are on an even row going to the down,a we are done
	}
} elseif ($direction == 8) {
	if (($location  <= 8) && ($location >= 0)) {
		return false;
	} elseif ((($location-8) %  15 <> 0) && (($location-15) %  15 <> 0)) {
		return true;
	} else {
		return false;
	}
} else {
echo 'No direction????';
}


}#end validspot function

function nextspot($location, $direction) {
if ($direction == 1) {
	if (oddrow) { 
		return $location + 1;
		} else {
		return false; #if we are on an even row going to the right, we are done
		}
} elseif ($direction == 2) {
return $location + 8;
} elseif ($direction == 3) {
	if (oddrow) { 
		return $location + 15;
		} else {
		return false; #if we are on an even row going to the down,a we are done
		}
} elseif ($direction == 4) {
return $location + 7;
} elseif ($direction == 5) {
	if (oddrow) { 
		return $location + 1;
		} else {
		return false; #if we are on an even row going to the left, we are done
		}
} elseif ($direction == 6) {
return $location - 8;
} elseif ($direction == 7) {
	if (oddrow) { 
		return $location - 15;
		} else {
		return false; #if we are on an even row going to the down,a we are done
		}
} elseif ($direction == 8) {
return $location - 7;
} else {
echo 'No direction????';
}

}#end nextspot function

function oddrow($location) {
if ((($location % 15)  <= 8) && (($location % 15) > 0)) {
return 1;
} else {
return 0;
}
}#end oddrow function

?>
