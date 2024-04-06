using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GPS : MonoBehaviour {
    public float latitude, longitude;
    public Text status;
    public static GPS Instance{set; get;}
    public bool succ = false;
    public bool scene2 = false;

	void Start () {
        Instance = this;
        DontDestroyOnLoad(gameObject);
        StartCoroutine(StartLocationService());
	}
	
    private IEnumerator StartLocationService()
    {
        
            if (!Input.location.isEnabledByUser)
            {
                status.text = "Please enable GPS";
                yield break;
            }
            Input.location.Start();
            int maxWait = 20;
            while (Input.location.status == LocationServiceStatus.Initializing && maxWait > 0)
            {
                yield return new WaitForSeconds(1);
                maxWait--;
            }
            if (maxWait <= 0)
            {
                status.text = "Time out";
                Debug.Log("Time out");
                yield break;
            }
            if (Input.location.status == LocationServiceStatus.Failed)
            {
                status.text = "can't determine device location";
                yield break;
            }        
        succ = true;
        scene2 = true;
        yield break;
    }
	void Update () {
        if (succ)
        {
            latitude = Input.location.lastData.latitude;
            longitude = Input.location.lastData.longitude;
        }
    }
}
