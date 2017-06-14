WORKING_DIR=pdf_images
cd $WORKING_DIR
rm ./*
curl -L $1 > entry.pdf
pdfimages -png entry.pdf img
