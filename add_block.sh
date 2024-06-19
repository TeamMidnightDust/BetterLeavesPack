# run this script with the mod namespace followed by the block-id to auto-generate the related files
NAMESPACE=$1
BLOCK=$2

if [ ! -d "assets/$NAMESPACE/" ]; then
  mkdir "assets/$NAMESPACE"
  mkdir "assets/$NAMESPACE/blockstates"
  mkdir "assets/$NAMESPACE/models"
  mkdir "assets/$NAMESPACE/models/block"
fi

BLOCKSTATES="assets/$NAMESPACE/blockstates/$BLOCK.json"

touch "$BLOCKSTATES"
echo "{  \"variants\": {    \"\": [" >> "$BLOCKSTATES"

for i in {1..8}
do
  printf "      { \"model\": \"$NAMESPACE:block/$BLOCK$i\" }," >> "$BLOCKSTATES"
  printf " { \"model\": \"$NAMESPACE:block/$BLOCK$i\", \"y\": 90 }," >> "$BLOCKSTATES"
  printf " { \"model\": \"$NAMESPACE:block/$BLOCK$i\", \"y\": 180 }," >> "$BLOCKSTATES"
  printf " { \"model\": \"$NAMESPACE:block/$BLOCK$i\", \"y\": 270 }" >> "$BLOCKSTATES"
  if (( i < 8 )); then
    echo "," >> "$BLOCKSTATES"
  else
    echo "" >> "$BLOCKSTATES"
  fi

  BLOCKFILE="assets/$NAMESPACE/models/block/$BLOCK$i.json"
  touch "$BLOCKFILE"
  echo "{\"parent\":\"block/leaves$i\",  \"textures\": {    \"0\":\"$NAMESPACE:block/$BLOCK\"  }}" >> "$BLOCKFILE"
done

echo "]}}" >> "$BLOCKSTATES"