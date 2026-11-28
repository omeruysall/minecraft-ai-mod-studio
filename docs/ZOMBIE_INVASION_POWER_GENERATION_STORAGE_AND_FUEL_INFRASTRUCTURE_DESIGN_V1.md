# Zombie Invasion — Power Generation, Storage and Fuel Infrastructure Design V1

Status: design specification. The user requested solar power, wind turbines, storable energy and gasoline storage. Exact numerical balance and implementation are not approved yet.

## 1. Design goals

Build a coherent survival energy economy. Players can generate electricity from renewable sources, store it, distribute it through a base network, and use liquid fuels as a dispatchable backup. Energy infrastructure should support safehouses, workshops, medical facilities, lighting, communications, defenses, vehicles and mobile bases.

The system must create meaningful choices without making renewable power either instantly unlimited or useless.

## 2. Electricity generation

### 2.1 Solar photovoltaic panels
- Panels generate electricity during daylight.
- Output depends on sunlight, weather, shade, orientation/placement where supported, panel tier, condition and damage.
- Dust, dirt, snow or damage may reduce output; maintenance and repair restore performance.
- Small portable panels can support limited devices; larger fixed arrays can support a safehouse or settlement.
- Solar generation falls at night and during poor weather; it must be paired with storage or backup generation for continuous loads.

### 2.2 Wind turbines
- Wind turbines generate electricity according to local wind conditions and turbine tier/condition.
- Exposed and elevated locations may provide better output; nearby obstructions can reduce it where the world simulation supports that calculation.
- Storms may increase wind generation but introduce structural damage or maintenance risk.
- Turbines require suitable components, installation space and repair materials.
- Include more than one scale, from compact units to larger base infrastructure.

### 2.3 Fuel-powered generators
- Generators provide controllable backup power when renewable generation and stored electricity are insufficient.
- Generator variants may use gasoline or diesel as specified by their engine design; fuels are not interchangeable unless an explicitly compatible conversion or engine is designed.
- Fuel consumption scales with generator load and condition.
- Generators require maintenance, produce noise and may attract nearby infected, creating a tactical trade-off.
- Exhaust and fire safety should matter in enclosed spaces; generators must not be treated as safe indoor appliances.

## 3. Electricity storage

- Portable batteries support small equipment and field use.
- Rechargeable battery units and battery banks store base-scale electricity.
- Higher-tier storage systems provide greater capacity and improved charge/discharge performance.
- Storage has finite capacity, condition and charging limits; it does not create energy.
- Battery charging, discharging and conversion losses may be represented in balance rules.
- Damaged storage can become unusable or hazardous according to the chosen realism level.
- Battery state, charge level and condition must be inspectable in the UI.

## 4. Fuel storage and handling

### 4.1 Fuel types
- Gasoline storage for compatible vehicles, tools and generators.
- Diesel storage for compatible diesel engines, heavy vehicles and generators.
- Other fuels may be introduced only when a defined gameplay use exists.
- Fuel types must be clearly labelled and compatibility validated; do not silently substitute one fuel for another.

### 4.2 Storage objects
- Small portable fuel cans for scavenging and transport.
- Sealed drums and intermediate fuel containers.
- Above-ground fuel tanks for settlement use.
- Larger fixed or buried storage tanks for advanced bases, subject to installation and safety requirements.
- Vehicle fuel tanks remain distinct from external storage containers.
- Storage capacity, current quantity, fuel type, condition and leakage status are visible.

### 4.3 Transfer and logistics
- Players can transfer fuel between compatible containers, tanks, generators and vehicles using appropriate tools or pumps.
- Advanced bases can use pumps and distribution equipment.
- Transfers must respect container capacity and fuel compatibility.
- Fuel can be scarce, scavenged, transported, traded where supported, and used in crafting or manufacturing only where explicitly required.

### 4.4 Risks
- Damaged containers may leak and lose stored fuel.
- Fuel near fire, sparks or combat damage can create fire hazards.
- Poorly planned storage can endanger a base.
- Fuel handling should be deliberate and communicated clearly to the player; avoid arbitrary instant explosions.

## 5. Electrical distribution and base management

- Generators, renewable sources, storage and consumers connect through a comprehensible power network.
- Cables, connectors, switches, breakers or distribution panels form the infrastructure progression.
- Players can turn circuits on and off and inspect generation, storage, consumption and faults.
- Power consumers include lighting, refrigerators/food preservation where implemented, medical equipment, workshop machines, communications, alarms, cameras, powered defenses, pumps and charging stations.
- Consumers may have priority tiers: critical, normal and optional. If available supply is insufficient, the player can decide what remains powered.
- Short circuits, damaged cables, overloads and weather exposure may cause faults and require repair.
- The system should support fixed bases and mobile bases such as the previously specified bus interior.

## 6. Progression and crafting

- The normal Minecraft Crafting Table remains the initial crafting station.
- Early stage: simple wiring, basic battery handling, portable lights and small fuel containers where recipes are appropriate.
- Intermediate stage: solar panels, compact wind turbines, basic generators, larger batteries, pumps and distribution components.
- Advanced stage: large solar arrays, robust wind turbines, high-capacity battery banks, industrial generators, fuel tanks, advanced power controls and repair equipment.
- Specialist workstations and rare components gate advanced technology. The player must scavenge, craft subassemblies and progress through the established workstation system.
- Do not make advanced infrastructure immediately craftable from starter materials.

## 7. Weather, day/night and world integration

- Solar production responds to day/night and weather systems.
- Wind production responds to wind and storms.
- Night-time demand makes storage planning meaningful.
- Seasonal conditions may affect production and maintenance, but exact seasonal modifiers remain to be balanced.
- Zombie threat integrates with power: lights, generators, machinery and alarms may create noise or visibility that changes risk. Renewable systems should generally be quieter than fuel generators.

## 8. User interface and telemetry

A power management interface should display:
- Current generation by source.
- Current consumption and connected consumers.
- Stored energy and available capacity.
- Battery charge/discharge state and condition.
- Fuel type, quantity and storage condition.
- Network faults, overloads and maintenance warnings.
- Estimated runtime for connected loads at the current supply level, where a meaningful estimate is available.

Do not display fabricated precision. The interface should explain why production changes (night, weather, shade, damage, fuel shortage or network fault).

## 9. Integration requirements

- Vehicle manufacturing and vehicle fuel systems must use compatible fuel definitions.
- Bus mobile-base interiors can contain batteries, compact solar equipment, generator modules or external connections where supported.
- Base construction can host panels, turbines, tanks, cables, lights, alarms and workshops.
- NPC dialogue can react to real power and fuel state, e.g. warn that the generator is out of fuel or the clinic has lost power. NPCs must not invent readings.
- Loot and scavenging can yield panels, batteries, cables, generators, fuel cans, drums, pumps and repair parts with condition states.

## 10. Acceptance criteria for a future implementation

1. Solar panels produce power only under valid light/weather conditions and stop or reduce output at night.
2. Wind turbines respond to wind conditions and their condition.
3. Generators consume the correct fuel and stop when fuel is exhausted or the unit fails.
4. Electricity can be stored and later consumed by connected devices.
5. Storage capacity and transfer limits are enforced.
6. Gasoline and diesel compatibility is validated.
7. Fuel can be stored in multiple container scales and transferred safely.
8. Power distribution exposes consumption, generation, storage and faults.
9. Players can prioritize critical consumers during shortages.
10. Renewable and fuel systems integrate with fixed bases and mobile bus bases.
11. NPC warnings reflect actual power/fuel state.
12. No UI or documentation claims the feature is implemented until it has been built and tested.

## 11. Open balance decisions

The following remain open for later design and playtesting: exact energy units, generation rates, battery capacities, fuel consumption, storage sizes, crafting costs, component tiers, network range/physical wiring rules, seasonal modifiers and failure probabilities.
