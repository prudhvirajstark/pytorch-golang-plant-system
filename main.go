package main

import (
	"fmt"
	"time"

	"github.com/prudhvirajstark/pytorch-golang-plant-system/ingestion"
)

func main() {
	fmt.Println("Automatic plant watering system simulation")
	ingestionMicroservice := ingestion.NewIngestionMicroservice("sensors/data")

	for {
		ingestionMicroservice.IngestData()

		time.Sleep(1 * time.Minute)
	}
}
