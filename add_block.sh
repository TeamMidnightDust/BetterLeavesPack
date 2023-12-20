# run this script with the modpack-id followed by the block-id to auto-generate the related files
MODPACK=$1
BLOCK=$2

if [ ! -d "assets/$MODPACK/" ]; then
  mkdir "assets/$MODPACK"
  mkdir "assets/$MODPACK/blockstates"
  mkdir "assets/$MODPACK/models"
  mkdir "assets/$MODPACK/models/block"
fi

BLOCKSTATES="assets/$MODPACK/blockstates/$BLOCK.json"

touch "$BLOCKSTATES"
echo "{\n  \"variants\": {\n    \"\": [" >> "$BLOCKSTATES"

for i in {1..8}
do
  printf "      { \"model\": \"$MODPACK:block/$BLOCK$i\" }" >> "$BLOCKSTATES"
  if (( i < 8 )); then
    echo "," >> "$BLOCKSTATES"
  else
    echo "" >> "$BLOCKSTATES"
  fi

  BLOCKFILE="assets/$MODPACK/models/block/$BLOCK$i.json"
  touch "$BLOCKFILE"
  echo "{\n  \"parent\":\"block/leaves$i\",\n  \"textures\": {\n    \"0\":\"$MODPACK:block/$BLOCK\"\n  }\n}" >> "$BLOCKFILE"
done

echo "    ]\n  }\n}" >> "$BLOCKSTATES"
