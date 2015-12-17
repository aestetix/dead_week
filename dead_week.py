# Fun DIY email generator to shut down a school district

# If it's not obvious, this is satire and should not actually be used for anything except metaphoric comedy.


# Personalize your threat:

date = 'Tuesday, 12/15/15'

villain = 'jihadist' 

school = 'L.A. Unified district'

places = ['Los Angeles', 'San Bernardino', 'Bakersfield', 'and San Diego']
places_var = ', '.join(places)

# email starts below this line

email = """
TO WHOM IT MAY CONCERN:

I am emailing you to inform you of the happenings on %(date)s. Something big is going down. Something very big. It will make national headlines. Perhaps, even international ones. You see, my last 4 years here at one of the district high schools has been absolute hell. Pure, unmitigated, agony. The bullying, the loneliness, the rejection... it is never-ending. And for what? Just because I'm 'different'?

No. No more. I am a devout Muslim, and was once against violence, but I have teamed up with a local %(villain)s cell as it is the only way I'll be able to accomplish my massacre the correct way. I would not be able to do it alone. Me, and my 32 comrades, will die tomorrow in the name of Allah. Every school in the %(school)s is being targeted. We have bombs hidden in lockers already at several schools. They are strategically placed and are meant to crumble the foundations of the very buildings that monger so much hate and discrimination. They are pressure cooker bombs, hidden in backpacks around the schools. They are loaded with 20 lbs. of gunpowder, for maximum damage. They will be detonated via Cell Phone. Not only are there bombs, but there are nerve gas agents set to go off at a specific time: during lunch hour. To top it off, my brothers in Allah and I have Kalashnikov rifles, Glock 18 Machine pistols, and multiple handheld grenades. The students at every school in the %(school)s will be massacred, mercilessly. And there is nothing you can do to stop it.

If you do end up trying to, by perhaps, beefing up security, or canceling classes for the day, it won't matter. Your security will not be able to stop us. We are an army of Allah. If you cancel classes, the bombings will take place regardless, and we will bring our guns to the streets and offices of %(places_var)s. 

I wish you the best luck. It is time to pray to allah, as this may be your last day.""" % { 'date': date, 'villain': villain, 'school': school, 'places_var': places_var }

print email
