<?php

init();

insertstates();

printarray();






function insertstates() {
global $thearray;
global $statearray;
global $counter;
foreach ($statearray as $state) {
#Try to stick it in there
	$counter=1;
	$stateletters = str_split($state);
	while (($counter != 0) || ($counter >= 113)) {
		if (($thearray[$location] == $stateletters[0]) || ($thearray[$location] == '0')) {
			if (trystate($state, $counter, 1)) {
			$statecounter++;
			} elseif (trystate($state, 2)) {
			$statecounter++;
			} elseif (trystate($state, 3)) {
			$statecounter++;
			} elseif (trystate($state, 4)) {
			$statecounter++;
			} elseif (trystate($state, 5)) {
			$statecounter++;
			} elseif (trystate($state, 6)) {
			$statecounter++;
			} elseif (trystate($state, 7)) {
			$statecounter++;
			} elseif (trystate($state, 8)) {
			$statecounter++;
			} else {
			echo "Could not fit $state at location $counter\n";
    			}
		} #If therer is a 0
	$counter++;
	}#end fhile
} #end each state
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
header("Content-type: text/plain"); 
global $thearray;
$thearray = array_fill(1,113, '0');
$filename = "/home/solarkennedy/xkyle.com/other/states";
global $statearray;
$statearray = file($filename);
}
function trystate($state, $location, $direction) {
global $thearray;
$stateletters = str_split($state);

if (fitstate($state, $location, $direction)) {
placestate($state, $location, $direction)
return true 
} else {
return false 
}


}#end function


function fitstate($state, $location, $direction) {
global $thearray;
$stateletters = str_split($state)
if (($thearray[$location] == $stateletters[0]) || ($thearray[$location] == '0')) {
	#The letter we need is already here!
	if (strlen($state) == 1) {
		return true;
	} elseif (validspot($location, $direction)) {
		$newstate = substr(-strlen($state) + 1)
		return fitstate($newstate, nextspot($location, $direction), $direction);
	} else {
		echo "im not sure how I ended up here";
	}
} else {
	return false;
	#The space was occupied
}#End letter check

} # end fitstate function


function placestate($state, $location, $direction) {
}#end placestate function

function validspot($location, $direction) {
if ($direction == 1) {
	if (oddrow) { 
		if (
	} else {
		return false; #if we are on an even row going to the right, we are done
	}
} elseif ($direction == 2 {
return $location + 8;
} elseif ($direction == 3 {
	if (oddrow) { 
		return $location + 15;
		} else {
		return false; #if we are on an even row going to the down,a we are done
		}
} elseif ($direction == 4 {
return $location + 7
} elseif ($direction == 5 {
	if (oddrow) { 
		return $location + 1;
		} else {
		return false; #if we are on an even row going to the left, we are done
} elseif ($direction == 6 {
return $location - 8
} elseif ($direction == 7 {
	if (oddrow) { 
		return $location - 15;
		} else {
		return false; #if we are on an even row going to the down,a we are done
		}
} elseif ($direction == 8 {
return $locationa - 7
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
} elseif ($direction == 2 {
return $location + 8;
} elseif ($direction == 3 {
	if (oddrow) { 
		return $location + 15;
		} else {
		return false; #if we are on an even row going to the down,a we are done
		}
} elseif ($direction == 4 {
return $location + 7
} elseif ($direction == 5 {
	if (oddrow) { 
		return $location + 1;
		} else {
		return false; #if we are on an even row going to the left, we are done
		}
} elseif ($direction == 6 {
return $location - 8
} elseif ($direction == 7 {
	if (oddrow) { 
		return $location - 15;
		} else {
		return false; #if we are on an even row going to the down,a we are done
		}
} elseif ($direction == 8 {
return $locationa - 7
} else {
echo 'No direction????';
}

}#end nextspot function

function oddrow($location) {
if (($location mod 15) <= 8) {
return 0;
} else {
return 1;
}
}#end oddrow function

?>
