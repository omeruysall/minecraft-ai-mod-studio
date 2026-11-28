# Real-Time Voice Communication Specification

**Document ID:** VOICE-RT-001  
**Version:** 1.0  
**Status:** Design draft — pending review and approval  
**Product:** Minecraft AI Mod Studio  
**Implementation status:** Not implemented  
**Last updated:** 2026-11-28

## 1. Purpose

Define the real-time voice interaction system that lets a creator discuss a Minecraft project naturally with the AI assistant. Voice is an alternative input/output mode for the same project conversation used by text; it must not create a disconnected assistant or separate project history.

This document defines product behavior and integration boundaries. It does not claim that microphone capture, speech recognition, speech synthesis, or real-time voice sessions are implemented.

## 2. Product principles

1. Voice is always user-initiated and visibly active only while the user has enabled it.
2. The user can switch between voice and text without losing conversation or project context.
3. The user can interrupt AI speech, pause listening, mute, and end a session.
4. Transcription is editable and correctable before uncertain speech becomes a confirmed project requirement.
5. The assistant must distinguish recognized speech from confirmed intent.
6. No project mutation, generation, publication, or approval is performed solely because the user spoke a phrase that could be ambiguous.
7. Critical actions require a clear, explicit confirmation step.
8. The voice system must disclose when speech processing is hosted or local, subject to actual deployment behavior.
9. Voice failure must not discard already captured text or project state.
10. The interface must be usable without voice; voice is an optional interaction mode.

## 3. User experience and session states

### 3.1 Entry and controls

The conversation composer should provide a clear voice action. During a session, expose:
- Listening state.
- Processing/transcription state.
- Assistant speaking state.
- Muted/paused state.
- Connection or provider unavailable state.
- End-session control.
- Text fallback control.

Controls must have accessible labels and clear visual state. Do not rely on color alone.

### 3.2 Session state model

Suggested states:
- IDLE: no active voice session.
- REQUESTING_PERMISSION: requesting microphone permission.
- CONNECTING: establishing the selected voice route.
- LISTENING: capturing user speech.
- TRANSCRIBING: converting speech to text, when applicable.
- THINKING: assistant is processing the turn.
- SPEAKING: assistant audio is playing.
- INTERRUPTED: current assistant output was interrupted.
- PAUSED: capture is paused or muted.
- RECONNECTING: recovering a transient connection.
- FAILED: session cannot continue.
- ENDED: user ended the session.

State transitions must be explicit and testable. The UI must not indicate LISTENING when microphone capture is inactive.

### 3.3 Turn-taking and interruption

- Support push-to-talk and hands-free modes if the selected runtime supports them.
- Push-to-talk should be available as a predictable fallback.
- In hands-free mode, use a configurable end-of-turn/silence policy where supported.
- User speech during assistant playback should interrupt or duck playback according to the selected mode.
- Provide a visible stop-speaking control.
- Do not treat background speech as an instruction when the session is paused or ended.
- Avoid accidental activation from ambient noise; activation and wake-word behavior remain configurable and require separate consent.

## 4. Speech processing architecture

Voice pipeline components:
1. Microphone capture and permission controller.
2. Audio session manager.
3. Voice transport/session connector.
4. Speech recognition or audio-capable model adapter.
5. Turn detector and interruption manager.
6. Conversation orchestrator.
7. Response text normalizer.
8. Speech synthesis or audio-capable response adapter.
9. Playback and audio focus manager.
10. Transcript and session event recorder.

The pipeline may use:
- Separate speech-to-text, text-model, and text-to-speech services.
- A real-time multimodal voice model.
- A local speech recognition/synthesis stack where supported.
- A hybrid route.

All routes must conform to the same conversation event contract and respect the AI Gateway's provider, privacy, and budget policies.

## 5. Audio and transcript event model

Each voice session should have a session ID. Each user/assistant turn should have a turn ID.

Events should support:
- Session started/ended.
- Microphone permission granted/denied.
- Audio capture started/stopped.
- Partial transcript.
- Final transcript.
- Transcript corrected by user.
- Assistant response text.
- Assistant audio started/ended.
- User interruption.
- Connection state changed.
- Provider error.
- Session recovery.

Transcript metadata should include:
- Transcript ID.
- Session and turn IDs.
- Speaker role.
- Text.
- Language, if detected with adequate confidence.
- Partial/final status.
- Recognition confidence where available.
- User-corrected flag.
- Timestamp.
- Source modality (voice or typed text).

Do not expose raw confidence as certainty. Low-confidence transcription should be marked for user review when it materially affects requirements.

## 6. Conversation integration

- Voice and text append to the same project conversation.
- The user can inspect a transcript after a turn.
- The user can edit a transcript where supported.
- Corrections update the conversation's recognized input with an auditable correction event.
- Project Architect receives normalized user intent only after the conversation layer has classified the turn.
- A transcript does not automatically become a confirmed requirement.
- If a spoken request is ambiguous, ask a concise clarification.
- The assistant should be able to speak a concise response while showing the full text response in the chat.
- Users can disable spoken responses and continue with transcription-only input.

## 7. Language and accessibility

The system should be designed for multilingual speech, with Turkish as a first-class target language. Additional language support depends on verified provider/runtime capabilities.

Language behavior:
- Allow manual language selection.
- Optionally detect language when supported.
- Allow switching language during a session.
- Preserve Minecraft identifiers, code symbols, version strings, and file names accurately where possible.
- Provide a correction mechanism for proper nouns and technical terms.
- Do not translate identifiers or code tokens unless explicitly requested.

Accessibility:
- Full text alternative for all voice interactions.
- Keyboard-accessible controls.
- Screen-reader labels for session states.
- Adjustable playback volume and speech rate where supported.
- Clear visual indication of microphone state.
- No voice-only confirmation for destructive or high-impact actions.

## 8. Privacy, permissions, and data handling

- Request microphone permission only when the user initiates voice.
- Explain why microphone access is needed.
- Show a persistent active-microphone indicator while capture is running.
- Provide immediate mute and end controls.
- Never activate microphone capture after a session has ended without a new user action.
- Disclose whether audio is processed locally or sent to a hosted provider.
- Disclose whether raw audio, transcripts, or derived metadata are retained, based on the actual provider and deployment configuration.
- Do not claim that audio is never stored unless verified for the selected route.
- Do not send audio to a different provider as fallback if that violates the user's privacy policy.
- Do not include credentials, API keys, or hidden secrets in audio prompts or logs.
- Team project permissions apply to transcripts and voice-derived project records.

## 9. Network, offline, and degraded modes

Possible modes:
- Hosted real-time voice.
- Hosted speech-to-text plus text AI plus text-to-speech.
- Local voice pipeline.
- Hybrid voice pipeline.
- Text-only fallback.

If connectivity is lost:
- Stop or pause hosted audio transmission.
- Preserve completed transcript segments.
- Clearly show the connection failure.
- Offer text input or a supported local mode.
- Resume only according to explicit session behavior; do not silently switch to a cloud provider with different privacy or cost implications.

Offline voice capabilities depend on installed local models, device resources, and tested language support. The product must not promise full offline voice until validated on supported hardware.

## 10. Performance and reliability targets

Exact numerical service-level targets are open decisions and must be set after provider/runtime evaluation. The implementation design should measure:
- Microphone start latency.
- Time to first partial transcript.
- End-of-turn detection latency.
- Time to first assistant audio.
- Interruption response latency.
- Audio dropouts and reconnect frequency.
- Transcription correction rate.
- Session completion/failure rate.

The UI should communicate when latency is caused by network, provider queue, model processing, or local device constraints where that information is available.

## 11. Error handling

Handle and explain:
- Microphone permission denied.
- No microphone device available.
- Microphone occupied by another application.
- Unsupported browser/device audio capability.
- Provider authentication or quota failure.
- Network loss.
- Speech recognition failure.
- Unsupported language.
- Speech synthesis failure.
- Audio playback blocked or unavailable.
- Session timeout.
- User cancellation.

If speech recognition fails but audio was captured, do not claim that the utterance was understood. Offer retry or text entry where possible.

## 12. Safety and high-impact actions

Voice may be used to discuss plans and request changes, but the system must require explicit confirmation for:
- Approving a project plan.
- Starting production when approval is required.
- Overwriting or deleting project files.
- Publishing or unpublishing content.
- Changing access permissions.
- Spending above the user's pre-authorized budget.
- Sending private project data to a newly selected provider.

For these actions, present a visible confirmation summary and require an explicit UI action or a clearly designed confirmation protocol. Ambient or low-confidence speech is insufficient.

## 13. Acceptance criteria

- Voice sessions are user-initiated and microphone state is always visible.
- Text and voice share the same project conversation and context.
- Users can interrupt assistant speech and end a session.
- Transcripts distinguish partial, final, and user-corrected text.
- Low-confidence or ambiguous speech is not silently converted into confirmed requirements.
- Turkish support is evaluated and tested before being advertised as production-ready.
- Provider routing obeys AI Gateway privacy and budget rules.
- Network failure preserves completed transcript content and provides text fallback.
- High-impact actions require explicit confirmation.
- Session states and errors are observable and testable.
- Voice can be disabled without disabling the rest of the product.

## 14. Open design decisions

1. First-release interaction mode: push-to-talk, hands-free, or both.
2. Initial voice architecture: real-time multimodal model versus separate speech-to-text, text AI, and text-to-speech services.
3. First-release Turkish speech providers and verified quality requirements.
4. Whether local speech recognition/synthesis is included in the first release.
5. Whether audio is retained at all, and the user's controls for retention/deletion.
6. Whether wake-word activation is excluded from the first release (recommended until explicit privacy and platform review).
7. Supported browser and mobile device matrix.
8. Target latency and reliability thresholds.
9. Whether voice sessions can continue in background and under which platform restrictions.
10. How spoken confirmation is designed for high-impact actions.

These decisions must be resolved through provider evaluation, privacy review, and target-device testing. They must not be assumed during implementation.

## 15. Implementation boundary

This is a design specification only. It does not assert that microphone capture, real-time transport, transcription, synthesis, interruption handling, or offline voice exists in the current application. Implementation begins only after the full design baseline is reviewed and explicitly approved.
