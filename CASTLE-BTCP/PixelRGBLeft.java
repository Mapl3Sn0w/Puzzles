//created by mapl3sn0w
import java.io.File;
import java.io.IOException;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class PixelRGBLeft {

	public static void main(String args[])throws IOException, FileNotFoundException {
				
		 PrintWriter pw = new PrintWriter(new File("C:\\FOLDERPATH\\output.csv"));
	     StringBuilder sb = new StringBuilder();
		
		BufferedImage image = null;
		File f = null;
		
		//read image file
		try{
			f = new File("C:\\FOLDERPATH\\Input.png");
			image = ImageIO.read(f);
			System.out.println("Reading complete.");
		}catch(IOException e){
			System.out.println("Error: "+e);
		}
		
		int width = image.getWidth();
		int height = image.getHeight();
		int r;
		int g;
		int b;
		
		for (int j=1;j<=440;j++)
		{
	
			for (int i=1;i<=110;i++)
			
			{
			
				for (int y=(j-1)*25; y <= (j-1)*25; y++)
				{
				
					for (int x=(i-1)*100; x <= (i-1)*100+7;x++)
						
					{
		
		        	 //get pixel value
					
		    	    int p = image.getRGB(x,y);
		
		    	    //get alpha
		    	    //a[x][y] = (p>>24) & 0xff;
		
		    	    //get red
		    	    r = (p>>16) & 0xff;
		    	  
		    	    //get green
		    	    g = (p>>8) & 0xff;
		
		    	    //get blue
		    	    b = p & 0xff;
		    	    
		    	    String rHex=Integer.toHexString(0x100|r).substring(1, 3);
		    	    String gHex=Integer.toHexString(0x100|g).substring(1, 3);
		    	    String bHex=Integer.toHexString(0x100|b).substring(1, 3);
		    	    
		    		sb.append(rHex);
		    		sb.append(',');
		    		sb.append(gHex);
		    		sb.append(',');
		    		sb.append(bHex);
		            sb.append('|');
		            
					}
					
				}
		        
		        //System.out.println("done!");
			}
			sb.append(System.getProperty("line.separator"));
		}
		//transfer pixel data to CSV file
        pw.write(sb.toString());
        pw.close();
		System.out.println("done!");
	}

}