#!/usr/bin/env bats

@test "build_filter should return a proper filter" {
  . solve.sh
  FILTER=`build_filter ANT CHAT ERA`
  echo $FILTER
  [[ "$FILTER" == "grep '.*a.*n.*t.*' | grep '.*c.*h.*a.*t.*' | grep '.*e.*r.*a.*' | cat" ]]
}

