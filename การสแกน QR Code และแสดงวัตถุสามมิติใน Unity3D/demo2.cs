IBarcodeReader barcodeReader = new BarcodeReader();
var result = barcodeReader.Decode(camTexture.GetPixels32(), camTexture.width, camTexture.height);
if( result.Text == "Jarutex" ){
  public GameObject fish, fish1
  fish1 = Instantiate(fish, new Vector3(0f, 0f, 0f), Quaternion.Euler(70, 0, 0));
}
