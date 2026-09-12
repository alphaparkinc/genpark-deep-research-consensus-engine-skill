from client import DeepResearchConsensusEngineClient

def main():
    client = DeepResearchConsensusEngineClient()
    res = client.verify_research_consensus()
    print("=== Deep Research Consensus Engine Output ===")
    print(f"Topic: {res['topic']}")
    print(f"Verdict: {res['verdict']} (Consensus Score: {res['consensus_score']*100:.1f}%)")
    print(f"Primary Claim: {res['primary_consensus_claim']}")
    print("\nSource Credibility Breakdown:")
    for c in res['evaluated_claims']:
        print(f"  [{c['net_credibility']:.3f}] ({c['source_url']}) -> {c['statement'][:60]}...")

if __name__ == '__main__':
    main()
