# UI Refactor Requirements & Progress Tracking

## 🎯 Project Goal
Transform abogen from a single-task interface to a modern, tabbed workflow with comprehensive queue management and better organization of settings.

## 📋 Core Requirements

### ✅ **1. Main Window Structure**
- [ ] **Tabbed Interface**: Main window with tabs at the top
  - Tab 1: "Processing" - Queue management and processing controls
  - Tab 2: "Settings" - All settings organized logically
- [ ] **Remove**: Current settings context menu entirely

### ✅ **2. Processing Tab Layout**
- [ ] **Left Sidebar**: Split into two sections
  - **Top**: Queue list with individual items
  - **Bottom**: Drop area for adding new items + Start Processing button
- [ ] **Main Content**: Selected queue item details
  - Chapter selection when item selected
  - Individual item logs when item selected
  - Item-specific controls

### ✅ **3. Queue Management**
- [ ] **Queue Items**: Individual items with their own progress bars
- [ ] **Item Status**: Display next to progress bar (pending/processing/completed/failed)
- [ ] **Drag & Drop Reordering**: Reorder queue items by dragging
- [ ] **Delete Items**: Remove items from queue (stops processing if active)
- [ ] **Duplicate Items**: Allow duplicate items (user responsibility)
- [ ] **Bulk Adding**: Multiple files create multiple queue items
- [ ] **Click Selection**: Click queue item to view/edit details

### ✅ **4. Processing Controls**
- [ ] **Global Controls**: Start All, Pause All, Resume All, Stop All
- [ ] **Individual Controls**: Start, Stop per queue item
- [ ] **Start Button**: Moved below drop area in sidebar
- [ ] **Global Status Bar**: Current status, global progress

### ✅ **5. Settings Tab Organization**
- [ ] **Output Settings Group**:
  - Save location (AudioBookshelf/Desktop/Custom)
  - Output path display
  - Project folder options
- [ ] **Audio Encoding Group**:
  - Format selection (WAV/FLAC/MP3/M4B/Opus)
  - Encoder selection (when applicable)
  - Bitrate selection (when applicable)
  - Separate chapters format
- [ ] **Voice & Speed Group**:
  - Voice selection (moved from main UI)
  - Voice mixer button (next to voice selection)
  - Speed setting (global for all queue items)
- [ ] **Subtitle Settings Group**:
  - Subtitle mode (Disabled/Sentence/Word-based)
  - Subtitle format (SRT/ASS variants)
- [ ] **Advanced Options Group**:
  - Replace single newlines option
  - spaCy segmentation option
  - Silent gaps option
  - Speed adjustment method
- [ ] **Pronunciation Settings Sidebar**:
  - Expandable/collapsible pronunciation editor
  - Real-time editing capabilities
  - Save/load pronunciation configs

### ✅ **6. File Handling**
- [ ] **Drop Area**: Support all current file types (EPUB, PDF, TXT, MD, SRT, ASS, VTT)
- [ ] **Bulk Processing**: Multiple files → multiple queue items
- [ ] **Current Functionality**: Maintain all existing file processing capabilities

### ✅ **7. Progress & Status**
- [ ] **Individual Progress**: Per-queue-item progress bars
- [ ] **Global Progress**: Overall processing progress
- [ ] **Status Display**: Current operation status in status bar
- [ ] **Detailed Logs**: Per-item logs in main content area

## 🚀 Implementation Steps

### **Phase 1: Core Infrastructure** 
- [x] Create tabbed main window structure
- [ ] Implement basic queue model/manager
- [ ] Create sidebar layout with placeholder widgets

### **Phase 2: Queue Management**
- [ ] Implement queue item widgets with progress bars
- [ ] Add drag & drop reordering functionality  
- [ ] Add delete/duplicate item capabilities
- [ ] Implement queue item selection and detail view

### **Phase 3: Settings Consolidation**
- [ ] Create settings tab with grouped widgets
- [ ] Move all settings from context menu to settings tab
- [ ] Implement pronunciation settings sidebar
- [ ] Connect settings to queue processing

### **Phase 4: Processing Integration**
- [ ] Connect queue items to conversion system
- [ ] Implement individual item processing
- [ ] Add global and per-item controls
- [ ] Implement status tracking and progress reporting

### **Phase 5: File Handling & Bulk Operations**
- [ ] Update drag & drop to create multiple queue items
- [ ] Implement bulk file processing
- [ ] Maintain backward compatibility with current file support

### **Phase 6: Polish & Testing**
- [ ] Status bar with global progress
- [ ] UI polish and responsiveness
- [ ] Comprehensive testing
- [ ] Documentation updates

## 🔮 Long-term Goals (Future Implementation)

### **Multi-threading Support**
- [ ] Parallel processing of multiple queue items
- [ ] Background processing without blocking UI
- [ ] Thread-safe progress reporting

### **Persistent Queue & Resume Capability**  
- [ ] Save queue state to disk
- [ ] Resume interrupted processing after app restart
- [ ] Crash recovery with partial progress preservation
- [ ] Pause/resume individual jobs across sessions

### **Smart Audiobook Updates**
- [ ] Detect existing audiobooks in output directory
- [ ] Compare source changes (new/modified/removed chapters)
- [ ] Incremental updates without full re-processing
- [ ] Version control for audiobook revisions

## 📝 Implementation Notes

- **Git Strategy**: Each major step gets its own commit
- **Backward Compatibility**: Ensure existing functionality is preserved
- **Code Organization**: Separate UI components into logical modules
- **Testing**: Manual testing after each phase
- **User Experience**: Maintain familiar workflow while improving efficiency

## 🗑️ Deletion Criteria
This file will be deleted when:
- [x] All core requirements implemented
- [ ] All long-term goals implemented  
- [ ] UI refactor is complete and stable
- [ ] Documentation is updated to reflect new UI

---
*Last Updated: 2026-01-20*
*Status: Planning Phase - Ready to Begin Implementation*