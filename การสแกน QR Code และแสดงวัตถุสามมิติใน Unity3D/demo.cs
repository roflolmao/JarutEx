IBarcodeReader barcodeReader = new BarcodeReader();

IBarcodeReader barcodeReader = new BarcodeReader();
var result = barcodeReader.Decode(camTexture.GetPixels32(), camTexture.width, camTexture.height);
if( result.Text == "Jarutex" ){
  //Do something
}
