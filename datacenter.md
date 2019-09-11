# fa19-516-159

## Week 1

### E.Datacenter.2.b

The Microsoft Redmond Ridge datacenter is located in Redmond, Washington. It was created in 2009. 
The datacenter can generate approximately 17.3 MW.<sup>1</sup> One of the goals of the datacenter is to improve
Microsoft's energy efficiency. The results are apparent - the datacenter has lowered the company's
carbon footprint by 12,000 tons yearly, which is about 30% of the datacenter's total footprint.<sup>2</sup>
This total amount comes to  about 40,000 tons, which is equivalent to the carbon output of 8421 vehicles.<sup>3</sup>
Using the electricity cost estimate of 10 cents/kW<sup>4</sup>, the datacenter costs about $15,154,800 per year. 

#### Sources: 
1. <https://news.softpedia.com/news/Disparate-Microsoft-Server-Labs-Shift-to-Redmond-Ridge-1-121721.shtml>
2. <https://www.greenbiz.com/blog/2009/09/09/inside-microsofts-new-purpose-built-data-lab>
3. <https://www.reference.com/science/much-pollution-average-car-produce-7f2a3d41ed9d2689>
4. <https://www.schneider-electric.com/en/work/solutions/system/s1/data-center-and-network-systems/trade-off-tools/data-center-capacity-and-growth-planning-calculator/>

### E.Datacenter.3

My carbon footprint is 32,235 lbs. I was surprised by how much "single family housing" affected this metric.

### E.Datacenter.4
Thermal energy is the energy contained within an object due to the movements of atoms within that object. Thermal 
energy, therefore, can depend on a variety of factors, including the object's substance, temperature, and size. For
objects where the molecules are loosely bound, such as in gas or liquids, there is likely more thermal energy than 
a solid at the same temperature. There is likely more thermal energy in objects that are hotter than in objects of a 
similar size and nature. Objects that are larger will contain more thermal energy than their smaller counterparts.<sup>1</sup>

Google plans to use thermal energy storage to cool the servers in one of its datacenters in Taiwan.<sup>2</sup>

#### Sources:
1. <https://www.chegg.com/homework-help/definitions/thermal-energy-2>
2. <https://serverlift.com/blog/thermal-energy-storage-technology-in-data-centers/>

### E.Datacenter.5

The purpose of a rear door heat exchanger (RDHx) is to remove the hot air that comes off of 
server racks. One implementation of an RDHx is called a "passive" RDHx. The term "passive" comes from
the fact that these heat exchangers do not have any moving parts (although they do require circulating water).
As a result, passive RDHx's demand less energy to operate and less maintenance. So, how does it work? 
Basically, server fans pump their hot air through the passive RDHx, which contains cold circulating water.
Heat is exchanged between these two components, and the air temperature is thereby reduced. The air temperature 
can be reduced by anywhere from 10-35 degrees Fahrenheit. The exact amount of air temperature 
change depends primarily on the size of the RDHx and the server's workload, but this cooling technique 
has been shown to decrease air temperature enough such that having dedicated "hot" and "cold" aisles is no longer 
necessary. Due to the simplicity of a passive RDHx, the installation is generally less complicated than the 
installation of other cooling units.<sup>1</sup>   

#### Source:
1. <https://datacenters.lbl.gov/sites/all/files/rdhx-doe-femp.pdf>

### E.Datacenter.8

In August of 2016, a fire broke out in a datacenter in Atlanta, Georgia. The primary user of this datacenter, 
Delta Airlines, was heavily affected. The fire affected both the primary and the secondary power generators,
which forced Delta to reboot approximately 500 of their servers.<sup>1</sup> Delta representatives reported
that the outage cost the company $150 million. Moreover, the outage affected over 2,000 flights over the course 
of three days.<sup>2</sup>

It appears that Delta did not have a redundant power architecture in their datacenter, which is part of what 
made this outage possible. In other words, the datacenter did not have a reliable backup for each of its components. 
The datacenter lost power when the Automatic Transfer Switch (ATS) - the unit 
that switches between primary and secondary power generators - caught fire. However, this should not
have crippled the datacenter, as it should have had a secondary ATS. It is suspected that if the datacenter
*did* have a secondary ATS, that it did not properly activate.<sup>3</sup>

#### Sources:
1. <https://arstechnica.com/information-technology/2016/08/data-center-disaster-disrupts-delta-airlines/>
2. <https://www.datacenterknowledge.com/archives/2016/09/08/delta-data-center-outage-cost-us-150m>
3. <http://up2v.nl/2016/08/16/a-reconstruction-of-the-delta-airlines-datacenter-outage/>