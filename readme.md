## Prototype Scope & Limitations

This prototype demonstrates a first-line, defensive approach to media risk assessment by surfacing contextual integrity indicators rather than performing automatic deepfake classification.

### Interpretation of Results
- **No Risk:** No integrity indicators detected in the uploaded media.
- **Medium Risk:** Platform processing, compression, or re-encoding detected. This does NOT imply manipulation, only reduced forensic confidence.
- **Elevated Risk:** Multiple integrity indicators detected; manual or ML-based verification is recommended.

### Boundary Cases
- Messaging-platform images (e.g., WhatsApp) may show Medium Risk due to metadata stripping and compression.
- Indoor or low-texture scenes (walls, floors, skin) can exhibit compression artifacts despite being authentic.
- Screen captures or re-photographed screens typically trigger Elevated Risk due to loss of original media integrity.
- Device-level camera processing (HDR, noise reduction) can result in Medium Risk even for directly uploaded images.


### Design Rationale
In defence and security systems, false positives are more dangerous than missed detections. The prototype intentionally avoids auto-classifying media as fake and instead provides risk context to support informed decision-making.

### Future Work

The current prototype focuses on reliable, first-layer risk indicators. In future iterations, the system will be expanded into a full, production-grade defence platform with the following components:

- **AI/ML-based Deepfake Detection:** Integration of trained deep learning models (PyTorch, Hugging Face) for image and video deepfake detection, including spatial and temporal analysis.
- **Advanced Media Forensics:** Frequency-domain analysis, artifact localization, and cross-frame consistency checks for improved detection accuracy.
- **Content Provenance & Consent:** Adoption of standards such as C2PA for cryptographic content provenance, authenticity verification, and consent tracking.
- **Scalable Backend Infrastructure:** FastAPI-based services with secure storage (PostgreSQL, object storage), caching, and audit logging.
- **Secure Deployment:** Containerized services using Docker, supporting cloud and on-premise defence deployments.

These components are planned to be integrated incrementally, following extensive validation to minimize false positives.


