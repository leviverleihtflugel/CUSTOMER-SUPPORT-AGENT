# streamlit_app.py
# -*- coding: utf-8 -*-

import streamlit as st
from llm_connection.llm_client import LLMClient
from agent.nodes.classify_question import QuestionClassifier
from agent.nodes.extract_intent import IntentExtractor
from agent.nodes.detect_sentiment import SentimentDetector
from agent.nodes.priority_scoring import PriorityScorer
from agent.nodes.logger import ConversationLogger
from agent.nodes.knowledge_base_search import KnowledgeBaseSearcher
from agent.nodes.summary_generator import SummaryGenerator  # Yeni dugum eklendi!

# LLM ve dugumleri baslat
llm_client = LLMClient()
classifier = QuestionClassifier()
intent_extractor = IntentExtractor()
sentiment_detector = SentimentDetector()
priority_scorer = PriorityScorer()
logger = ConversationLogger()
knowledge_searcher = KnowledgeBaseSearcher()
summary_generator = SummaryGenerator()  # Cevap Ozeti baslatildi

st.set_page_config(page_title="CUSTOMER SUPPORT AGENT", page_icon="??")
st.title("CUSTOMER SUPPORT AGENT")

user_input = st.text_input("SORUNUZU YAZIN:")

if st.button("CEVAPLA") and user_input:
    with st.spinner('YANIT HAZIRLANIYOR...'):
        category = classifier.classify(user_input)
        intent = intent_extractor.extract(user_input)
        sentiment = sentiment_detector.detect(user_input)
        priority = priority_scorer.score(user_input)
        kb_answer = knowledge_searcher.search(user_input)

        if kb_answer:
            response = kb_answer
        else:
            response = llm_client.generate_response(user_input)

        # Cevap Ozeti Uret
        summary = summary_generator.summarize(response)

        # Sonuclari ekranda goster
        st.subheader("SINIFLANDIRILAN KATEGORI:")
        st.success(category.capitalize())

        st.subheader("BELIRLENEN AMAC:")
        st.success(intent.capitalize())

        st.subheader("ALGILANAN DUYGU:")
        st.success(sentiment.capitalize())

        st.subheader("ONCELIK SEVIYESI:")
        st.success(priority.capitalize())

        st.subheader("YANIT:")
        st.success(response)

        st.subheader("CEVAP OZETI:")
        st.success(summary)

        # LOG dosyasina yaziliyor
        logger.log(
            user_input=user_input,
            category=category,
            intent=intent,
            sentiment=sentiment,
            priority=priority,
            response=response
        )
