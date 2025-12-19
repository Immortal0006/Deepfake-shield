## Prototype Scope & Limitations

This prototype demonstrates a first-line, defensive approach to media risk assessment using contextual indicators rather than automatic deepfake detection.

### Boundary Cases
- Platform-compressed images (e.g., WhatsApp re-shares) may show medium risk due to metadata loss and re-encoding.
- Images with large smooth regions (walls, floors, skin, low-texture scenes) can exhibit forensic artifacts despite being authentic.
- The prototype intentionally avoids auto-classifying media as fake to reduce false positives.

### Design Rationale
In defence and security systems, false positives can cause greater harm than missed detections. Therefore, this prototype focuses on surfacing risk indicators and recommending verification, rather than making final judgments.

### Future Work
- Integration of trained deepfake detection models (image and video)
- Temporal and multimodal analysis
- Confidence scoring based on large-scale validation datasets
