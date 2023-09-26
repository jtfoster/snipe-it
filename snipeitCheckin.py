import requests
import time
import logging
import config

logging.basicConfig(
    filename="checkin_logging.log",
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d, %(levelname)s, %(module)s, %(funcName)s, %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

apiKey = config.apiKey
url = "https://rummel.snipe-it.io/api/v1/hardware/"

headers = {
    "authorization": "Bearer " + apiKey,
    "accept": "application/json",
    "content-type": "application/json",
}

def checkin():
    #assetTag = [Your asset tags go here]

    for tag in assetTag:
      print(assetTag)
      print("")
      print("==========================")
      print("Checking in asset " + tag)
      searchURL = url + "bytag/" + str(tag)
      print(searchURL)
      searchResponse = requests.request("GET", searchURL, headers=headers).json()
      time.sleep(0.5)
      print(searchResponse)

      if "id" in searchResponse:
        print(searchResponse)
        checkinURL = url + str(searchResponse["id"]) + "/checkin"
        print(checkinURL)
        checkinResponse = requests.post(checkinURL, headers=headers).json()
        print(checkinResponse)
        logging.info("Checked in asset %s" % str(tag))
        print ("ID")

    else:
            print("Exiting...")


def main():
    checkin()


if __name__ == "__main__":
    main()
