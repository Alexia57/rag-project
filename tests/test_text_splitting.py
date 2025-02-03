def test_text_splitting(text: str, chunk_size: int = 1000, chunk_overlap: int = 250):
    try:
        print("🔄 Splitting text into chunks...")
        chunks = []
        for i in range(0, len(text), chunk_size - chunk_overlap):
            chunks.append(text[i:i + chunk_size])
        print(f"✅ Text split into {len(chunks)} chunks!")
        return chunks
    except Exception as e:
        print(f"❌ Failed to split text: {e}")
        return []

# Test with a dummy text
dummy_text = "This is a long text. " * 100
test_text_splitting(dummy_text)
