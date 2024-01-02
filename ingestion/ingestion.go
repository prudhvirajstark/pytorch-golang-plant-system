package ingestion

import (
	"fmt"
	"os"
)

type IngestionMicroservice struct {
	SensorDataDir string
}

func NewIngestionMicroservice(sensorDataDir string) *IngestionMicroservice {
	return &IngestionMicroservice{
		SensorDataDir: sensorDataDir,
	}
}

func (ingest *IngestionMicroservice) IngestData() error {
	files, err := os.ReadDir(ingest.SensorDataDir)
	if err != nil {
		return err
	}

	for _, file := range files {
		fmt.Println(file)
	}
	return nil
}
