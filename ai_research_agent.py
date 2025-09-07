import streamlit as st
import json
import time
from datetime import datetime
from typing import List, Dict, Any

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .summary-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .source-item {
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        border-left: 4px solid #1f77b4;
    }
    .progress-bar {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

class WebSearcher:
    def __init__(self, num_results=5, time_filter="None"):
        self.num_results = num_results
        self.time_filter = time_filter
        
    def search(self, query: str) -> List[Dict[str, str]]:
        """Return mock search results for demonstration purposes"""
        mock_results = [
            {
                "title": f"Recent Breakthrough in {query}",
                "url": "https://example.com/breakthrough",
                "snippet": f"Scientists have made a significant breakthrough in {query} that could change the industry."
            },
            {
                "title": f"Understanding {query}: A Comprehensive Guide",
                "url": "https://example.com/guide",
                "snippet": f"This comprehensive guide explains the fundamentals of {query} and its applications."
            },
            {
                "title": f"The Future of {query}: Predictions and Trends",
                "url": "https://example.com/future",
                "snippet": f"Experts predict major advancements in {query} over the next decade that will transform the field."
            },
            {
                "title": f"Challenges and Opportunities in {query}",
                "url": "https://example.com/challenges",
                "snippet": f"While {query} offers tremendous potential, researchers face several challenges that need to be addressed."
            },
            {
                "title": f"{query} Applications in Modern Technology",
                "url": "https://example.com/applications",
                "snippet": f"From healthcare to finance, {query} is being applied in innovative ways across various industries."
            }
        ]
        return mock_results[:self.num_results]

class ContentExtractor:
    def __init__(self):
        pass
    
    def extract_from_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Extract mock content from URLs for demonstration"""
        extracted_data = []
        
        for i, url in enumerate(urls):
            try:
                # Create mock extracted content
                article_data = {
                    "title": f"Research Article #{i+1}",
                    "url": url,
                    "content": f"This is a detailed article about the research topic. It contains valuable information, statistics, and insights that would be summarized by an AI system in a real implementation. The content includes key findings, methodology, and conclusions that researchers would find valuable for their work.",
                    "publish_date": f"2024-0{i+1}-15",
                    "author": f"Researcher {i+1}",
                    "domain": "example.com"
                }
                
                extracted_data.append(article_data)
                
            except Exception as e:
                print(f"Error extracting content from {url}: {e}")
                extracted_data.append({
                    "title": "Failed to extract title",
                    "url": url,
                    "content": f"Failed to extract content from {url}",
                    "publish_date": "Unknown",
                    "author": "Unknown",
                    "domain": "example.com"
                })
        
        return extracted_data

class ContentSummarizer:
    def __init__(self, format="Bullet points", tone="Neutral"):
        self.format = format
        self.tone = tone
    
    def summarize(self, content: str) -> str:
        """Generate mock summary for demonstration purposes"""
        if self.format == "Bullet points":
            return f"""
## Summary of Research Content (Bullet Points)

Based on analysis of multiple sources, here are the key findings:

- **Major breakthrough**: Significant progress has been made in this field recently
- **Key applications**: This technology is being applied across various industries
- **Future potential**: Experts predict transformative impact over the next decade
- **Current challenges**: Several technical hurdles remain to be solved
- **Research focus**: Most studies are concentrating on improving efficiency and scalability

*Note: In a production environment with API access, this would be generated by an AI model based on the actual content from real web sources.*
"""
        elif self.format == "Paragraph":
            return f"""
## Summary of Research Content (Paragraph Format)

Recent advancements in this field have demonstrated significant potential for transforming various industries. Researchers have made breakthroughs that address previous limitations while opening up new applications. The technology shows promise for solving complex problems more efficiently than previous approaches. However, challenges remain in scaling these solutions and ensuring their practical implementation. Ongoing research focuses on optimizing performance and expanding the range of possible applications.

*Note: In a production environment with API access, this would be generated by an AI model based on the actual content from real web sources.*
"""
        else:  # Detailed report
            return f"""
## Comprehensive Research Report

### Executive Summary
This report provides an overview of current developments, highlighting both opportunities and challenges in the field. The technology has reached a maturity level where practical applications are becoming feasible.

### Key Findings
1. **Performance Improvements**: Recent studies show a 30-40% increase in efficiency compared to previous approaches.
2. **Diverse Applications**: The technology is being adapted for use in healthcare, finance, and environmental monitoring.
3. **Research Investment**: Funding for related projects has increased by 25% year-over-year.

### Challenges and Limitations
- **Scalability Issues**: Current implementations struggle with large-scale deployment.
- **Regulatory Hurdles**: Compliance with existing frameworks remains a concern.
- **Technical Complexity**: Implementation requires specialized expertise.

### Future Outlook
Experts predict widespread adoption within 5-7 years as technical challenges are addressed and costs decrease.

*Note: In a production environment with API access, this would be generated by an AI model based on the actual content from real web sources.*
"""

class ResearchAgent:
    def __init__(self, num_results=5, time_filter="None", summary_format="Bullet points", tone="Neutral"):
        self.num_results = num_results
        self.time_filter = time_filter
        self.summary_format = summary_format
        self.tone = tone
        
        # Initialize components
        self.searcher = WebSearcher(num_results=num_results, time_filter=time_filter)
        self.extractor = ContentExtractor()
        self.summarizer = ContentSummarizer(format=summary_format, tone=tone)
    
    def search_web(self, query: str) -> List[Dict[str, str]]:
        """Perform web search for the given query"""
        return self.searcher.search(query)
    
    def extract_content(self, search_results: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """Extract content from search results"""
        return self.extractor.extract_from_urls([result['url'] for result in search_results])
    
    def analyze_content(self, extracted_content: List[Dict[str, Any]]) -> str:
        """Analyze extracted content"""
        combined_content = "\n\n".join([
            f"Source: {item.get('title', 'Unknown')}\nContent: {item.get('content', 'No content')}"
            for item in extracted_content
        ])
        return combined_content
    
    def generate_summary(self, analysis: str) -> str:
        """Generate summary from analyzed content"""
        return self.summarizer.summarize(analysis)

def main():
    # Set page configuration
    st.set_page_config(
        page_title="AI Research Agent",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize session state
    if 'research_history' not in st.session_state:
        st.session_state.research_history = []
    if 'current_research' not in st.session_state:
        st.session_state.current_research = None

    # Header
    st.markdown('<h1 class="main-header">🔍 AI Research Agent</h1>', unsafe_allow_html=True)
    st.markdown("### Your smart research assistant for gathering, summarizing, and synthesizing information")

    # Sidebar for settings and history
    with st.sidebar:
        st.header("Settings")
        
        # Search settings
        num_results = st.slider("Number of search results", 3, 10, 5)
        time_filter = st.selectbox(
            "Time filter",
            ["None", "Past week", "Past month", "Past year"]
        )
        
        # Summarization settings
        summary_format = st.radio(
            "Summary format",
            ["Bullet points", "Paragraph", "Detailed report"]
        )
        
        # Tone selection
        tone = st.selectbox(
            "Tone",
            ["Neutral", "Technical", "Simplified", "Academic", "Conversational"]
        )
        
        st.divider()
        st.header("Research History")
        
        if st.session_state.research_history:
            for i, research in enumerate(st.session_state.research_history):
                if st.button(f"{research['topic'][:30]}... - {research['timestamp']}", key=f"history_{i}"):
                    st.session_state.current_research = research
        else:
            st.info("No research history yet.")

    # Main content area
    tab1, tab2 = st.tabs(["New Research", "Results"])

    with tab1:
        st.markdown('<div class="sub-header">Enter your research topic</div>', unsafe_allow_html=True)
        
        research_topic = st.text_area(
            "Research Query",
            placeholder="e.g., 'Recent advancements in quantum computing' or 'Benefits of intermittent fasting'",
            height=100
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start Research", type="primary", use_container_width=True):
                if research_topic:
                    with st.spinner("Initializing research agent..."):
                        # Initialize research agent
                        agent = ResearchAgent(
                            num_results=num_results,
                            time_filter=time_filter,
                            summary_format=summary_format,
                            tone=tone
                        )
                        
                        # Create progress bar
                        progress_bar = st.progress(0, text="Starting research...")
                        
                        # Perform research
                        try:
                            progress_bar.progress(10, text="Searching the web...")
                            search_results = agent.search_web(research_topic)
                            
                            progress_bar.progress(30, text="Extracting content...")
                            extracted_content = agent.extract_content(search_results)
                            
                            progress_bar.progress(60, text="Analyzing content...")
                            analysis = agent.analyze_content(extracted_content)
                            
                            progress_bar.progress(90, text="Generating summary...")
                            summary = agent.generate_summary(analysis)
                            
                            progress_bar.progress(100, text="Research complete!")
                            
                            # Store results
                            research_result = {
                                "topic": research_topic,
                                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "summary": summary,
                                "sources": extracted_content,
                                "settings": {
                                    "num_results": num_results,
                                    "time_filter": time_filter,
                                    "summary_format": summary_format,
                                    "tone": tone
                                }
                            }
                            
                            st.session_state.research_history.append(research_result)
                            st.session_state.current_research = research_result
                            
                            st.success("Research completed successfully!")
                            time.sleep(1)
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"An error occurred during research: {str(e)}")
                else:
                    st.warning("Please enter a research topic.")
        
        with col2:
            if st.button("Clear Input", use_container_width=True):
                st.rerun()

    with tab2:
        if st.session_state.current_research:
            research = st.session_state.current_research
            
            st.markdown(f"### Research Topic: {research['topic']}")
            st.caption(f"Research conducted on: {research['timestamp']}")
            
            # Display summary
            st.markdown("### Summary")
            st.markdown('<div class="summary-box">', unsafe_allow_html=True)
            st.markdown(research['summary'])
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Display sources
            st.markdown("### Sources")
            for i, source in enumerate(research['sources']):
                with st.expander(f"Source {i+1}: {source.get('title', 'Untitled')}"):
                    st.markdown(f"**URL:** {source.get('url', 'N/A')}")
                    st.markdown(f"**Domain:** {source.get('domain', 'N/A')}")
                    if 'publish_date' in source:
                        st.markdown(f"**Published:** {source['publish_date']}")
                    if 'author' in source:
                        st.markdown(f"**Author:** {source['author']}")
                    
                    st.markdown("**Extracted Content:**")
                    st.markdown(f"> {source.get('content', 'No content extracted.')[:500]}...")
            
            # Export options
            st.markdown("### Export Results")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Export as Markdown"):
                    # Generate markdown content
                    markdown_content = f"# Research Report: {research['topic']}\n\n"
                    markdown_content += f"*Generated on: {research['timestamp']}*\n\n"
                    markdown_content += "## Summary\n\n"
                    markdown_content += research['summary'] + "\n\n"
                    markdown_content += "## Sources\n\n"
                    
                    for i, source in enumerate(research['sources']):
                        markdown_content += f"{i+1}. **{source.get('title', 'Untitled')}**\n"
                        markdown_content += f"   - URL: {source.get('url', 'N/A')}\n"
                        if 'publish_date' in source:
                            markdown_content += f"   - Published: {source['publish_date']}\n"
                        if 'author' in source:
                            markdown_content += f"   - Author: {source['author']}\n"
                        markdown_content += "\n"
                    
                    # Create download button
                    st.download_button(
                        label="Download Markdown",
                        data=markdown_content,
                        file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                        mime="text/markdown"
                    )
            
            with col2:
                st.info("PDF export coming soon!")
        else:
            st.info("No research results to display. Please conduct a research first.")

if __name__ == "__main__":
    main()