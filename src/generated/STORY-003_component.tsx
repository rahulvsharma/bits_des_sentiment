import React, { useState } from "react";
import axios from "axios";

interface SentimentResult {
  text: string;
  positive: number;
  negative: number;
  neutral: number;
  compound: number;
}

export const SentimentAnalysisComponent: React.FC = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState<SentimentResult | null>(null);
  const [loading, setLoading] = useState(false);

  const analyzeSentiment = async () => {
    setLoading(true);
    try {
      const response = await axios.post("/api/sentiment/analyze", {
        text: text,
        source: "news",
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error analyzing sentiment:", error);
    } finally {
      setLoading(false);
    }
  };

  const getSentimentColor = (compound: number) => {
    if (compound > 0.1) return "bg-green-100";
    if (compound < -0.1) return "bg-red-100";
    return "bg-yellow-100";
  };

  return (
    <div className="sentiment p-6">
      <h1 className="text-2xl font-bold mb-4">Market Sentiment Analysis</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text to analyze"
        className="w-full border p-3 mb-4 rounded"
        rows={4}
      />
      <button
        onClick={analyzeSentiment}
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div
          className={`mt-6 p-4 rounded ${getSentimentColor(result.compound)}`}
        >
          <p className="font-bold mb-2">Sentiment Scores:</p>
          <p>Positive: {(result.positive * 100).toFixed(1)}%</p>
          <p>Negative: {(result.negative * 100).toFixed(1)}%</p>
          <p>Neutral: {(result.neutral * 100).toFixed(1)}%</p>
          <p className="font-bold mt-2">
            Compound: {result.compound.toFixed(3)}
          </p>
        </div>
      )}
    </div>
  );
};

export default SentimentAnalysisComponent;
