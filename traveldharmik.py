# Travel Planning Assistant Chatbot
# Created by: [Your Name] and [Partner's Name]
# Group Project - Basic Chatbot Creation

def travel_planning_bot():
    print("=" * 50)
    print("    ✈️  TRAVEL PLANNING ASSISTANT  ✈️")
    print("=" * 50)
    print("I can help with destinations, packing, budgets & travel tips!")
    print("Type 'quit' to end our travel planning session")
    print("-" * 50)
    
    while True:
        user_input = input("\nWhat travel help do you need? ").lower().strip()
        
        # Exit condition
        if user_input == 'quit':
            print("Happy travels! Bon voyage! 🌍")
            break
            
        # 1. Beach destinations
        elif 'beach' in user_input or 'island' in user_input:
            print("Great beach destinations: Bali, Thailand, Maldives, Greece, or Mexico. Don't forget sunscreen!")
            
        # 2. Budget travel
        elif 'budget' in user_input or 'cheap' in user_input:
            print("Budget tips: Travel offseason, use hostels, cook your own meals, walk instead of taxi.")
            
        # 3. Packing tips
        elif 'pack' in user_input or 'what to bring' in user_input:
            print("Pack light: Roll clothes, use packing cubes, bring versatile items, and always pack a first-aid kit.")
            
        # 4. Adventure travel
        elif 'adventure' in user_input or 'hiking' in user_input:
            print("Adventure spots: New Zealand, Costa Rica, Nepal, Peru. Pack good shoes and a waterproof jacket!")
            
        # 5. City destinations
        elif 'city' in user_input or 'urban' in user_input:
            print("Top cities: Tokyo, Paris, New York, Barcelona, Istanbul. Get city passes for attractions.")
            
        # 6. Solo travel
        elif 'solo' in user_input or 'alone' in user_input:
            print("Solo travel tips: Stay in social hostels, join free walking tours, trust your instincts, share itinerary.")
            
        # 7. Family travel
        elif 'family' in user_input or 'kids' in user_input:
            print("Family-friendly: Orlando, Singapore, London. Book apartments, pack snacks, plan kid-friendly activities.")
            
        # 8. Travel documents
        elif 'passport' in user_input or 'visa' in user_input:
            print("Check passport validity (6+ months), research visa requirements, make copies of important documents.")
            
        # 9. Food destinations
        elif 'food' in user_input or 'cuisine' in user_input:
            print("Food capitals: Italy, Thailand, Japan, Mexico, Vietnam. Try street food for authentic local flavors!")
            
        # 10. Romantic getaways
        elif 'romantic' in user_input or 'honeymoon' in user_input:
            print("Romantic spots: Paris, Santorini, Venice, Maldives. Book sunset dinners and private tours.")
            
        # 11. Winter destinations
        elif 'winter' in user_input or 'snow' in user_input:
            print("Winter wonderlands: Switzerland, Canada, Norway, Japan. Pack layers and thermal wear.")
            
        # 12. Travel safety
        elif 'safe' in user_input or 'security' in user_input:
            print("Safety tips: Research areas, avoid flashing valuables, know emergency numbers, get travel insurance.")
            
        # 13. Default response
        else:
            print("I can help with destinations, packing, budgets, safety, or specific types of travel. What are you planning?")

# Start the chatbot
if __name__ == "__main__":
    travel_planning_bot()